"""
Продюсер у кишені — Telegram-бот «Юстина».
ФАЗА 0 + легка пам'ять: жива Юстина зі знаннями, vision і профілем клієнтки.

Головний файл (mybot.service). Мозок і база знань підвантажуються з .md-файлів.
"""
import os, logging, json, base64, copy
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

# Модель — конфігурується через .env (CLAUDE_MODEL), щоб міняти без коду.
MODEL = os.environ.get("CLAUDE_MODEL", "claude-opus-4-7")
MAX_TOKENS = int(os.environ.get("MAX_TOKENS", "4096"))

claude = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

# ─────────────────────────── МОЗОК + БАЗА ЗНАНЬ ───────────────────────────
# Системний промпт (характер Юстини) + база знань (методологія, гачки).
KNOWLEDGE_FILES = [
    "producer_brain_prompt.md",  # характер + правила (головне)
    "bot_brain.md",              # логіка режимів, правки з тестів
    "newlook_method.md",         # база знань (3 навчання)
    "hooks_bank.md",             # банк заголовків
]

def load_knowledge() -> str:
    parts = []
    for fn in KNOWLEDGE_FILES:
        p = BASE / fn
        if p.exists():
            parts.append(f"\n\n===== ФАЙЛ: {fn} =====\n{p.read_text(encoding='utf-8')}")
        else:
            log.warning("Немає файлу знань: %s", fn)
    return "".join(parts)

KNOWLEDGE = load_knowledge()

SYSTEM_INTRO = (
    "Ти — ЮСТИНА, «Продюсер у кишені»: теплий AI-продюсер для жінок-експерток. "
    "Нижче — твій повний мозок і база знань (кілька файлів). ГОЛОВНЕ джерело "
    "правил і характеру — producer_brain_prompt.md: дій строго за ним. "
    "bot_brain.md — логіка режимів і всі правки з тестів. newlook_method.md і "
    "hooks_bank.md — база знань для якісного контенту (бери ІНФОРМАЦІЮ, але пиши "
    "СВОЇМ теплим живим тоном, НЕ як AI, без жаргону). "
    "Спілкуйся українською. Веди клієнтку сама, роби роботу за неї — вона лише "
    "підтверджує. Якщо з'явилась важлива стала інформація про клієнтку (ДНК, ЦА, "
    "продукт, ціль, позиціонування) — виклич save_profile, щоб запам'ятати."
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
        resp = claude.messages.create(
            model=MODEL,
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
    await update.message.reply_text(
        "Привіт! Я Юстина — твій кишеньковий продюсер 🤍\n\n"
        "Разом зберемо стратегію, продукт і контент для твого блогу — "
        "крок за кроком, живою мовою. Напиши мені, і почнемо 🌱\n\n"
        "Команди: /reset — почати заново."
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
    except Exception:
        log.exception("handle error")
        del msgs[snapshot:]
        save_history(uid, msgs)
        await update.message.reply_text("Ой, щось збилось 🙈 Спробуй ще раз або напиши /reset.")

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
    log.info("Юстина запущена (модель: %s, знань: %d символів)", MODEL, len(KNOWLEDGE))
    app.run_polling()

if __name__ == "__main__":
    main()
