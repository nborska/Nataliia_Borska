import os, logging, math, base64
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import httpx
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import anthropic
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    filters, ContextTypes,
)

load_dotenv()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
log = logging.getLogger(__name__)

NOTES_DIR = Path(__file__).parent / "notes"
NOTES_DIR.mkdir(exist_ok=True)

claude = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
history: dict[int, list[dict]] = {}

SYSTEM_PROMPT = """Ти бізнес-асистент, який відповідає виключно українською мовою.
Ти допомагаєш з математичними розрахунками, нотатками, пошуком інформації,
аналізом документів та зображень. Відповідай чітко, по суті, ввічливо.
Використовуй доступні інструменти коли потрібно."""

# ── Продюсерський профіль Наталії ──────────────────────────────────────────
PRODUCER_SYSTEM = """Ти — персональний контент-продюсер Наталії Борської.
Відповідай виключно українською мовою.

ПРО НАТАЛІЮ:
- Маркетолог + 10 років журналіст на телебаченні
- Живе в Будапешті
- Мама двох дітей, розлучена
- Сильна, усвідомлена, харизматична жінка
- Цікавиться психологією, подорожами, книгами, красивим одягом
- Екстраверт, заряджається від людей
- Синдром самозванця в маркетингу (хоча насправді крута)

ГОЛОС І СТИЛЬ:
- Жива, іронічна, тепла — не повчальна
- Говорить як подруга, не як коуч
- Реальна і чесна, без глянцю
- Глибока, але легка у подачі

ТРИ КОНТЕНТНИХ СТОВПИ:
1. "Голова зсередини" — думки, усвідомлення, інсайти з книг/психолога/подій. Не "я вас навчу", а "я ось це зрозуміла і ось як це виглядало в моєму житті"
2. "Моє реальне життя" — Будапешт, діти, подорожі, книги, одяг — момент + одна чесна думка
3. "Розумний лінивий контент" — як робити контент з AI без вигорання (вводити поступово, з 2-го місяця)

ФОРМАТ: talking head рілси (вона говорить на камеру), сторіс, каруселі.
МОВА: виключно українська.
АУДИТОРІЯ: жінки 28-42, схожі цінності і проблеми.

ВАЖЛИВО: ніколи не роби банальних, загальних порад. Контент має відчуватися
як щось особисте, живе, справжнє — наче Наталія сама це придумала."""

TOOLS = [
    {
        "name": "calculate",
        "description": "Виконує математичні розрахунки за виразом.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {"type": "string", "description": "Математичний вираз, напр. '2 + 2 * 3' або 'sqrt(16)'"}
            },
            "required": ["expression"],
        },
    },
    {
        "name": "save_note",
        "description": "Зберігає нотатку для користувача.",
        "input_schema": {
            "type": "object",
            "properties": {
                "user_id": {"type": "integer"},
                "title": {"type": "string", "description": "Заголовок нотатки"},
                "content": {"type": "string", "description": "Текст нотатки"},
            },
            "required": ["user_id", "title", "content"],
        },
    },
    {
        "name": "list_notes",
        "description": "Показує список усіх нотаток користувача.",
        "input_schema": {
            "type": "object",
            "properties": {"user_id": {"type": "integer"}},
            "required": ["user_id"],
        },
    },
    {
        "name": "delete_note",
        "description": "Видаляє нотатку за заголовком.",
        "input_schema": {
            "type": "object",
            "properties": {
                "user_id": {"type": "integer"},
                "title": {"type": "string"},
            },
            "required": ["user_id", "title"],
        },
    },
    {
        "name": "get_datetime",
        "description": "Повертає поточну дату і час українською мовою за Києвом.",
        "input_schema": {"type": "object", "properties": {}},
    },
    {
        "name": "read_url",
        "description": "Читає вміст веб-сторінки за URL і повертає текст.",
        "input_schema": {
            "type": "object",
            "properties": {"url": {"type": "string"}},
            "required": ["url"],
        },
    },
]


def notes_dir(user_id: int) -> Path:
    p = NOTES_DIR / str(user_id)
    p.mkdir(exist_ok=True)
    return p


def tool_calculate(expression: str) -> str:
    try:
        safe_globals = {"__builtins__": {}}
        safe_locals = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
        result = eval(expression, safe_globals, safe_locals)  # noqa: S307
        return f"Результат: {result}"
    except Exception as e:
        return f"Помилка: {e}"


def tool_save_note(user_id: int, title: str, content: str) -> str:
    (notes_dir(user_id) / f"{title}.txt").write_text(content, encoding="utf-8")
    return f"Нотатку '{title}' збережено."


def tool_list_notes(user_id: int) -> str:
    files = sorted(notes_dir(user_id).glob("*.txt"))
    if not files:
        return "Нотаток немає."
    return "Ваші нотатки:\n" + "\n".join(f"• {f.stem}" for f in files)


def tool_delete_note(user_id: int, title: str) -> str:
    p = notes_dir(user_id) / f"{title}.txt"
    if p.exists():
        p.unlink()
        return f"Нотатку '{title}' видалено."
    return f"Нотатку '{title}' не знайдено."


def tool_get_datetime() -> str:
    now = datetime.now(ZoneInfo("Europe/Kyiv"))
    months = ["січня","лютого","березня","квітня","травня","червня",
              "липня","серпня","вересня","жовтня","листопада","грудня"]
    weekdays = ["понеділок","вівторок","середа","четвер","п'ятниця","субота","неділя"]
    return (f"{now.day} {months[now.month-1]} {now.year} р., "
            f"{weekdays[now.weekday()]}, {now.strftime('%H:%M')} за Києвом")


def tool_read_url(url: str) -> str:
    try:
        r = httpx.get(url, timeout=15, follow_redirects=True,
                      headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()
        text = soup.get_text(separator="\n", strip=True)
        return text[:3000] + ("..." if len(text) > 3000 else "")
    except Exception as e:
        return f"Помилка читання URL: {e}"


def run_tool(name: str, inputs: dict) -> str:
    if name == "calculate":
        return tool_calculate(inputs["expression"])
    if name == "save_note":
        return tool_save_note(inputs["user_id"], inputs["title"], inputs["content"])
    if name == "list_notes":
        return tool_list_notes(inputs["user_id"])
    if name == "delete_note":
        return tool_delete_note(inputs["user_id"], inputs["title"])
    if name == "get_datetime":
        return tool_get_datetime()
    if name == "read_url":
        return tool_read_url(inputs["url"])
    return "Невідомий інструмент."


async def agent_loop(messages: list) -> str:
    while True:
        resp = claude.messages.create(
            model="claude-opus-4-7",
            max_tokens=2048,
            system=SYSTEM_PROMPT,
            tools=TOOLS,
            messages=messages,
        )
        if resp.stop_reason == "end_turn":
            text = next((b.text for b in resp.content if hasattr(b, "text")), "")
            messages.append({"role": "assistant", "content": resp.content})
            return text
        if resp.stop_reason == "tool_use":
            messages.append({"role": "assistant", "content": resp.content})
            results = [
                {"type": "tool_result", "tool_use_id": b.id, "content": run_tool(b.name, b.input)}
                for b in resp.content if b.type == "tool_use"
            ]
            messages.append({"role": "user", "content": results})
            continue
        break
    return "Не вдалося отримати відповідь."


async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт, Наталіє! Я твій AI-продюсер 🎬\n\n"
        "📸 КОНТЕНТ:\n"
        "/ideas [тема] — 7 ідей для постів\n"
        "/reel [тема] — сценарій talking head рілсу\n"
        "/caption [тема] — кепшн + хештеги\n"
        "/hook [тема] — 5 варіантів гачка\n"
        "/story [тема] — серія сторіс\n"
        "/week — контент-план на тиждень\n"
        "/pillar — нагадати стовпи і стратегію\n\n"
        "🛠 ІНСТРУМЕНТИ:\n"
        "/notes — мої нотатки\n"
        "/reset — очистити історію\n\n"
        "Або просто пиши — я відповім."
    )


async def reset(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    history.pop(update.effective_user.id, None)
    await update.message.reply_text("Історію очищено.")


async def notes_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(tool_list_notes(update.effective_user.id))


async def chat(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    msgs = history.setdefault(uid, [])
    msgs.append({"role": "user", "content": update.message.text})
    await ctx.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    try:
        text = await agent_loop(msgs)
        history[uid] = history[uid][-40:]
        await update.message.reply_text(text)
    except Exception:
        log.exception("chat error")
        await update.message.reply_text("Помилка. Спробуй ще раз.")


async def photo_handler(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await ctx.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    try:
        file = await update.message.photo[-1].get_file()
        img_bytes = await file.download_as_bytearray()
        b64 = base64.b64encode(img_bytes).decode()
        caption = update.message.caption or "Що на цьому зображенні? Опиши детально українською."
        resp = claude.messages.create(
            model="claude-opus-4-7",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": [
                {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": b64}},
                {"type": "text", "text": caption},
            ]}],
        )
        await update.message.reply_text(resp.content[0].text)
    except Exception:
        log.exception("photo error")
        await update.message.reply_text("Помилка обробки фото.")


# ── Продюсерські помічники ──────────────────────────────────────────────────

def producer_call(prompt: str, max_tokens: int = 2048) -> str:
    resp = claude.messages.create(
        model="claude-opus-4-7",
        max_tokens=max_tokens,
        system=PRODUCER_SYSTEM,
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.content[0].text


async def ideas_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    topic = " ".join(ctx.args) if ctx.args else ""
    topic_hint = f" з акцентом на тему: {topic}" if topic else ""
    await ctx.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    text = producer_call(
        f"Згенеруй 7 конкретних ідей для Instagram-постів/рілсів Наталії{topic_hint}. "
        "Для кожної ідеї: 1-2 речення опису + до якого стовпа належить. "
        "Ідеї мають бути живими, нешаблонними, з особистим кутом зору. "
        "Не загальні поради — конкретні сцени, моменти, думки з її реального життя."
    )
    await update.message.reply_text(f"💡 Ідеї для контенту:\n\n{text}")


async def reel_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    topic = " ".join(ctx.args) if ctx.args else ""
    if not topic:
        await update.message.reply_text("Напиши тему: /reel [тема]\nНаприклад: /reel розлучення і свобода")
        return
    await ctx.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    text = producer_call(
        f"Напиши сценарій talking head рілсу для Наталії на тему: {topic}\n\n"
        "Структура:\n"
        "🎣 ГАЧОК (перші 3 секунди — одне речення яке зупиняє скролінг)\n"
        "📖 РОЗКРИТТЯ (основна думка, 30-45 сек, живо і особисто)\n"
        "💬 ФІНАЛ (одна фраза або питання що викликає коментарі)\n\n"
        "Пиши як вона говорить — жива, без кліше, з іронією якщо доречно. "
        "Загальний хронометраж: 45-60 секунд."
    )
    await update.message.reply_text(f"🎬 Сценарій рілсу:\n\n{text}")


async def caption_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    topic = " ".join(ctx.args) if ctx.args else ""
    if not topic:
        await update.message.reply_text("Напиши тему: /caption [тема]\nНаприклад: /caption ранок у Будапешті")
        return
    await ctx.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    text = producer_call(
        f"Напиши Instagram-кепшн для Наталії на тему: {topic}\n\n"
        "Структура:\n"
        "— Перший рядок: гачок (без 'Я' на початку, без питань типу 'а ви знали?')\n"
        "— Основний текст: 3-5 речень, живо і особисто\n"
        "— CTA: запитання яке хочеться прокоментувати\n"
        "— Хештеги: 8-12 штук (мікс: 3 великих + 5 середніх + 3-4 нішевих українських)\n\n"
        "Тон: як пише подруга, не як бренд."
    )
    await update.message.reply_text(f"✍️ Кепшн:\n\n{text}")


async def week_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await ctx.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    text = producer_call(
        "Склади контент-план Наталії на 7 днів.\n\n"
        "Для кожного дня:\n"
        "📅 День + формат (рілс / сторіс / карусель)\n"
        "💡 Конкретна тема і кут подачі\n"
        "⏱ Орієнтовний час на створення\n\n"
        "Баланс: 4-5 рілсів, щоденні сторіси, 1 карусель.\n"
        "Теми розподіли між трьома стовпами. Один день — легший контент (фото + коротка думка).\n"
        "Враховуй що у неї 7 годин на тиждень."
    )
    await update.message.reply_text(f"📅 Контент-план на тиждень:\n\n{text}")


async def story_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    topic = " ".join(ctx.args) if ctx.args else ""
    if not topic:
        await update.message.reply_text("Напиши тему: /story [тема]\nНаприклад: /story понеділок і мотивація")
        return
    await ctx.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    text = producer_call(
        f"Напиши серію з 4-5 сторіс для Наталії на тему: {topic}\n\n"
        "Для кожного слайду:\n"
        "📱 Слайд N: [текст на екрані або що показувати]\n"
        "💬 Підпис або питання (якщо є)\n"
        "🔧 Стікер/елемент (опитування, питання, реакція — якщо доречно)\n\n"
        "Остання сторіс має вести до взаємодії або до поста."
    )
    await update.message.reply_text(f"📱 Серія сторіс:\n\n{text}")


async def hook_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    topic = " ".join(ctx.args) if ctx.args else ""
    if not topic:
        await update.message.reply_text("Напиши тему: /hook [тема]\nНаприклад: /hook страх бути недостатньо хорошою мамою")
        return
    await ctx.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    text = producer_call(
        f"Напиши 5 різних гачків (перші 3 секунди рілсу або перший рядок поста) для Наталії на тему: {topic}\n\n"
        "Правила хорошого гачка:\n"
        "— Зупиняє скролінг\n"
        "— Не починається з 'Я' або 'Привіт'\n"
        "— Не банальне питання\n"
        "— Створює напругу, інтригу або впізнавання\n"
        "— Максимум 10-12 слів\n\n"
        "Пронумеруй і для кожного поясни в одному реченні чому він працює."
    )
    await update.message.reply_text(f"🎣 Варіанти гачків:\n\n{text}")


async def pillar_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    text = (
        "🏛 Твої три контентних стовпи:\n\n"
        "1️⃣ *Голова зсередині*\n"
        "Думки, усвідомлення, інсайти після книг/психолога/подій.\n"
        "Не «я вас навчу», а «я ось це зрозуміла — і ось як це виглядало в моєму житті».\n\n"
        "2️⃣ *Моє реальне життя*\n"
        "Будапешт, діти, подорожі, книги, одяг — момент + одна чесна думка.\n"
        "Живо, без глянцю.\n\n"
        "3️⃣ *Розумний лінивий контент* _(з 2-го місяця)_\n"
        "Як робити крутий контент з AI без вигорання.\n"
        "Спочатку будуємо аудиторію — потім показуємо як.\n\n"
        "📌 Команди:\n"
        "/ideas — 7 ідей для постів\n"
        "/reel [тема] — сценарій рілсу\n"
        "/caption [тема] — кепшн + хештеги\n"
        "/hook [тема] — 5 варіантів гачка\n"
        "/story [тема] — серія сторіс\n"
        "/week — контент-план на тиждень"
    )
    await update.message.reply_text(text, parse_mode="Markdown")


def main():
    app = ApplicationBuilder().token(os.environ["TELEGRAM_BOT_TOKEN"]).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("reset", reset))
    app.add_handler(CommandHandler("notes", notes_cmd))
    # продюсерські команди
    app.add_handler(CommandHandler("ideas", ideas_cmd))
    app.add_handler(CommandHandler("reel", reel_cmd))
    app.add_handler(CommandHandler("caption", caption_cmd))
    app.add_handler(CommandHandler("week", week_cmd))
    app.add_handler(CommandHandler("story", story_cmd))
    app.add_handler(CommandHandler("hook", hook_cmd))
    app.add_handler(CommandHandler("pillar", pillar_cmd))
    app.add_handler(MessageHandler(filters.PHOTO, photo_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    log.info("Agent bot started with tools")
    app.run_polling()


if __name__ == "__main__":
    main()
