"""
Продюсер у кишені — Telegram-бот «Юстина».
ФАЗА 0 + легка пам'ять: жива Юстина зі знаннями, vision і профілем клієнтки.

Головний файл (mybot.service). Мозок і база знань підвантажуються з .md-файлів.
"""
import os, logging, json, base64, copy, re
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

# прибрати проксі (як у попередніх версіях — інакше ламається SDK)
for _v in ("HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy", "ALL_PROXY", "all_proxy"):
    os.environ.pop(_v, None)

from dotenv import load_dotenv
import anthropic
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes,
)

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)

BASE = Path(__file__).parent
DATA = BASE / "data"
DATA.mkdir(exist_ok=True)

# Модель. Бот САМ підбирає робочу зі списку (моделі час від часу
# застарівають — це рятує від "падінь"). Можна зафіксувати через .env CLAUDE_MODEL.
MODEL_CANDIDATES = [m for m in [
    os.environ.get("CLAUDE_MODEL"),
    "claude-sonnet-4-5",
    "claude-sonnet-4-20250514",
    "claude-3-5-sonnet-latest",
    "claude-3-5-sonnet-20241022",
    "claude-3-5-haiku-latest",
] if m]
_working_model = None  # запам'ятовуємо першу робочу

def _create(**kwargs):
    """Виклик Claude із автопідбором робочої моделі."""
    global _working_model
    order = ([_working_model] if _working_model else []) + \
            [m for m in MODEL_CANDIDATES if m != _working_model]
    last_err = None
    for m in order:
        try:
            resp = claude.messages.create(model=m, **kwargs)
            if _working_model != m:
                _working_model = m
                log.info("Робоча модель: %s", m)
            return resp
        except (anthropic.NotFoundError, anthropic.BadRequestError) as e:
            last_err = e
            log.warning("Модель %s не підійшла: %s", m, e)
            continue
    raise last_err if last_err else RuntimeError("Немає доступних моделей")
MAX_TOKENS = int(os.environ.get("MAX_TOKENS", "4096"))

claude = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

# ─────────────────────────── МОЗОК + БАЗА ЗНАНЬ ───────────────────────────
# ОПТИМІЗАЦІЯ: у системний промпт іде лише КОМПАКТНИЙ мозок (~5к токенів
# замість ~60к). Повні файли — довідник, підвантажується на вимогу через
# інструмент lookup_knowledge (див. нижче). Здешевлює у ~10 разів.
COMPACT_FILE = "brain_compact.md"
REFERENCE_FILES = ["hooks_bank.md", "newlook_method.md", "bot_brain.md"]

def load_compact() -> str:
    p = BASE / COMPACT_FILE
    if p.exists():
        return p.read_text(encoding="utf-8")
    # запасний варіант — старий повний промпт
    p2 = BASE / "producer_brain_prompt.md"
    log.warning("Немає %s, вантажу producer_brain_prompt.md", COMPACT_FILE)
    return p2.read_text(encoding="utf-8") if p2.exists() else ""

KNOWLEDGE = load_compact()

def _load_reference_sections():
    """Розбиваємо довідкові файли на секції (за заголовками ##/#) для пошуку."""
    sections = []
    for fn in REFERENCE_FILES:
        p = BASE / fn
        if not p.exists():
            continue
        title, cur = fn, []
        for line in p.read_text(encoding="utf-8").split("\n"):
            if line.startswith("# ") or line.startswith("## "):
                if cur:
                    sections.append((title, "\n".join(cur)))
                title = line.lstrip("# ").strip()
                cur = [line]
            else:
                cur.append(line)
        if cur:
            sections.append((title, "\n".join(cur)))
    return sections

REFERENCE_SECTIONS = _load_reference_sections()

def lookup_knowledge(query: str, max_chars: int = 4500) -> str:
    """Пошук релевантних секцій у повній базі знань (на вимогу моделі)."""
    qwords = {w for w in re.findall(r"[\w']+", query.lower()) if len(w) > 3}
    if not qwords:
        return "Уточни запит."
    scored = []
    for title, text in REFERENCE_SECTIONS:
        low = (title + " " + text).lower()
        score = sum(low.count(w) for w in qwords)
        if any(w in title.lower() for w in qwords):
            score += 5
        if score:
            scored.append((score, title, text))
    scored.sort(key=lambda x: x[0], reverse=True)
    out, total = [], 0
    for _, title, text in scored[:4]:
        chunk = text[:1800]
        if total + len(chunk) > max_chars:
            break
        out.append(f"### {title}\n{chunk}")
        total += len(chunk)
    return "\n\n".join(out) if out else "Нічого конкретного не знайдено — відповідай зі стислого мозку."

SYSTEM_INTRO = (
    "Ти — ЮСТИНА, «Продюсер у кишені». Нижче — твій КОМПАКТНИЙ мозок (стисла "
    "робоча версія методу). Дій строго за ним. Коли потрібні ДЕТАЛІ (повний банк "
    "гачків, приклади сценаріїв/прогрівів, розширені фреймворки) — виклич "
    "інструмент lookup_knowledge(query), НЕ вигадуй з голови. "
    "Пиши СВОЇМ теплим живим тоном, українською, НЕ як AI, без жаргону. Веди "
    "клієнтку сама. Важливе про клієнтку (ДНК, ЦА, продукт, ціль, позиціонування) "
    "зберігай через save_profile і не перепитуй."
)

def system_blocks(uid: int) -> list:
    """Системний контекст: інтро + база знань (кешується) + профіль клієнтки."""
    prof = load_profile(uid)
    prof_txt = (
        "ПРОФІЛЬ ЦІЄЇ КЛІЄНТКИ (твоя пам'ять — використовуй, НЕ перепитуй вже відоме):\n"
        + (json.dumps(prof, ensure_ascii=False, indent=2) if prof
           else "(поки порожній — заповнюй через save_profile у міру знайомства)")
    )
    return [
        {"type": "text", "text": SYSTEM_INTRO},
        {"type": "text", "text": KNOWLEDGE, "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": prof_txt},
    ]

# ─────────────────────────── ПАМ'ЯТЬ (диск) ───────────────────────────
def _hist_path(uid: int) -> Path: return DATA / f"hist_{uid}.json"
def _prof_path(uid: int) -> Path: return DATA / f"profile_{uid}.json"

def load_history(uid: int) -> list:
    p = _hist_path(uid)
    try:
        return json.loads(p.read_text(encoding="utf-8")) if p.exists() else []
    except Exception:
        return []

def save_history(uid: int, msgs: list) -> None:
    try:
        _hist_path(uid).write_text(json.dumps(msgs, ensure_ascii=False), encoding="utf-8")
    except Exception:
        log.exception("save_history")

def load_profile(uid: int) -> dict:
    p = _prof_path(uid)
    try:
        return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
    except Exception:
        return {}

def save_profile_dict(uid: int, prof: dict) -> None:
    _prof_path(uid).write_text(json.dumps(prof, ensure_ascii=False, indent=2), encoding="utf-8")

# ─────────────────────────── ІНСТРУМЕНТИ ───────────────────────────
TOOLS = [
    {
        "name": "save_profile",
        "description": "Зберегти/оновити поле профілю клієнтки (пам'ять). Викликай, "
                       "коли з'явилась важлива СТАЛА інформація: ДНК, ЦА, карта сенсів, "
                       "продукт, ціль, позиціонування, стан, що працює.",
        "input_schema": {
            "type": "object",
            "properties": {
                "key": {"type": "string", "description": "поле, напр. 'ДНК','ЦА','продукт','ціль','позиціонування'"},
                "value": {"type": "string", "description": "вміст поля"},
            },
            "required": ["key", "value"],
        },
    },
    {
        "name": "get_profile",
        "description": "Повернути весь збережений профіль клієнтки.",
        "input_schema": {"type": "object", "properties": {}},
    },
    {
        "name": "get_datetime",
        "description": "Поточна дата, день тижня і час за Києвом (для планування контенту).",
        "input_schema": {"type": "object", "properties": {}},
    },
    {
        "name": "lookup_knowledge",
        "description": "Знайти ДЕТАЛЬНИЙ матеріал у повній базі знань: банк ~200 гачків, "
                       "готові сценарії/сюжети, повні фреймворки лекцій, приклади прогрівів, "
                       "структура лід-магніту, приклади продаючих шапок тощо. Викликай, коли "
                       "стислого мозку не вистачає і потрібні конкретні деталі/приклади.",
        "input_schema": {
            "type": "object",
            "properties": {"query": {"type": "string", "description": "що шукаємо, напр. 'гачки про помилки', 'каркас сторітелу через біль', 'структура лід-магніту'"}},
            "required": ["query"],
        },
    },
]

def _get_datetime() -> str:
    now = datetime.now(ZoneInfo("Europe/Kyiv"))
    months = ["січня","лютого","березня","квітня","травня","червня",
              "липня","серпня","вересня","жовтня","листопада","грудня"]
    weekdays = ["понеділок","вівторок","середа","четвер","п'ятниця","субота","неділя"]
    return (f"{now.day} {months[now.month-1]} {now.year}, "
            f"{weekdays[now.weekday()]}, {now.strftime('%H:%M')} за Києвом")

def run_tool(uid: int, name: str, inp: dict) -> str:
    if name == "save_profile":
        prof = load_profile(uid)
        prof[inp["key"]] = inp["value"]
        save_profile_dict(uid, prof)
        return f"✔ Запам'ятала у профіль: {inp['key']}"
    if name == "get_profile":
        prof = load_profile(uid)
        return json.dumps(prof, ensure_ascii=False, indent=2) if prof else "Профіль поки порожній."
    if name == "get_datetime":
        return _get_datetime()
    if name == "lookup_knowledge":
        return lookup_knowledge(inp.get("query", ""))
    return "Невідомий інструмент."

# ─────────────────────────── АГЕНТ-ЦИКЛ ───────────────────────────
def _blocks_to_dicts(content_blocks) -> list:
    result = []
    for b in content_blocks:
        if b.type == "text":
            if b.text and b.text.strip():
                result.append({"type": "text", "text": b.text})
        elif b.type == "tool_use":
            result.append({"type": "tool_use", "id": b.id, "name": b.name, "input": b.input})
    return result

def _clean_messages(messages: list) -> list:
    """Прибрати порожні текстові блоки (інакше API 400), не мутуючи історію."""
    result = []
    for msg in messages:
        content = msg.get("content")
        if isinstance(content, list):
            clean = [
                copy.copy(b) for b in content
                if not (isinstance(b, dict) and b.get("type") == "text"
                        and not (b.get("text") or "").strip())
            ]
            if clean:
                result.append({**msg, "content": clean})
        else:
            if isinstance(content, str) and content.strip():
                result.append(copy.copy(msg))
    return result

def agent_loop(uid: int, messages: list) -> str:
    while True:
        resp = _create(
            max_tokens=MAX_TOKENS,
            system=system_blocks(uid),
            tools=TOOLS,
            messages=_clean_messages(messages),
        )
        content_dicts = _blocks_to_dicts(resp.content)

        if resp.stop_reason == "tool_use":
            if content_dicts:
                messages.append({"role": "assistant", "content": content_dicts})
            tool_results = [
                {"type": "tool_result", "tool_use_id": b.id,
                 "content": run_tool(uid, b.name, b.input)}
                for b in resp.content if b.type == "tool_use"
            ]
            messages.append({"role": "user", "content": tool_results})
            continue

        # end_turn (або інше) — повертаємо текст
        text = next((b["text"] for b in content_dicts if b["type"] == "text"), "")
        if content_dicts:
            messages.append({"role": "assistant", "content": content_dicts})
        return text or "Готово 🤍"

# ─────────────────────────── ХЕНДЛЕРИ ───────────────────────────
async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    """Починаємо: Юстина сама вітається за сценарієм і ставить перше питання."""
    uid = update.effective_user.id
    _hist_path(uid).unlink(missing_ok=True)  # свіжий старт
    seed = [{"role": "user", "content": [{"type": "text", "text": (
        "(Клієнтка щойно відкрила бота і натиснула /start. Привітайся як Юстина "
        "за сценарієм ВСТУПУ з мозку: коротко й тепло поясни, хто ти і як ми "
        "працюємо, покажи шлях (🌱 фундамент → 💎 продукт → ✍️ контент → "
        "⚙️ автоворонка), і ОДРАЗУ постав ПЕРШЕ питання — 'навіщо тобі блог?' "
        "з варіантами. Далі веди сама. Не згадуй, що ти AI-модель.)"
    )}]}]
    await ctx.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    try:
        reply = agent_loop(uid, seed)
        save_history(uid, seed[-40:])
        for chunk in _split(reply, 4000):
            await update.message.reply_text(chunk)
    except Exception as e:
        log.exception("start error")
        await update.message.reply_text(
            "Привіт! Я Юстина — твій кишеньковий продюсер 🤍\n"
            "Напиши мені «почнімо» — і зберемо твою стратегію крок за кроком 🌱\n"
            f"(тех. деталь: {type(e).__name__}: {str(e)[:200]})"
        )

async def reset(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    _hist_path(uid).unlink(missing_ok=True)
    await update.message.reply_text("Історію розмови очищено 🤍 (профіль лишився). Почнімо спочатку?")

async def handle(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    text = (update.message.text or update.message.caption or "").strip()

    # зібрати контент повідомлення (текст + фото, якщо є)
    content_parts = []
    if update.message.photo:
        try:
            file = await update.message.photo[-1].get_file()
            img = await file.download_as_bytearray()
            b64 = base64.b64encode(img).decode()
            content_parts.append({"type": "image", "source": {
                "type": "base64", "media_type": "image/jpeg", "data": b64}})
        except Exception:
            log.exception("photo download")
    content_parts.append({"type": "text", "text": text or "(клієнтка надіслала зображення)"})

    msgs = load_history(uid)
    snapshot = len(msgs)
    msgs.append({"role": "user", "content": content_parts})

    await ctx.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    try:
        reply = agent_loop(uid, msgs)
        msgs[:] = msgs[-40:]  # тримаємо останні 40 повідомлень
        save_history(uid, msgs)
        # Telegram ліміт 4096 символів — ріжемо на частини
        for chunk in _split(reply, 4000):
            await update.message.reply_text(chunk)
    except Exception as e:
        log.exception("handle error")
        del msgs[snapshot:]
        save_history(uid, msgs)
        # тимчасово показуємо суть помилки — легше діагностувати на етапі запуску
        await update.message.reply_text(
            "Ой, щось збилось 🙈 Спробуй ще раз або напиши /reset.\n"
            f"(тех. деталь: {type(e).__name__}: {str(e)[:250]})"
        )

def _split(text: str, size: int) -> list:
    if len(text) <= size:
        return [text]
    out, cur = [], ""
    for line in text.split("\n"):
        if len(cur) + len(line) + 1 > size:
            if cur:
                out.append(cur)
            cur = line
        else:
            cur = f"{cur}\n{line}" if cur else line
    if cur:
        out.append(cur)
    return out

def main():
    app = ApplicationBuilder().token(os.environ["TELEGRAM_BOT_TOKEN"]).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("reset", reset))
    app.add_handler(MessageHandler((filters.TEXT | filters.PHOTO) & ~filters.COMMAND, handle))
    log.info("Юстина запущена (кандидати моделей: %s, знань: %d символів)",
             ", ".join(MODEL_CANDIDATES), len(KNOWLEDGE))
    app.run_polling()

if __name__ == "__main__":
    main()
