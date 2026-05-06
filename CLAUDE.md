# Telegram-бот на Claude

Головний файл — bot.py. Залежності — requirements.txt.

## Сервер
Бот працює на VPS DigitalOcean (167.99.213.201).
- Шлях: /root/nataliia_borska
- Сервіс: mybot.service (systemd)
- Автодеплой: /root/autodeploy.sh запускається щохвилини,
  робить git pull і перезапускає сервіс при змінах.
- Git relay: cmdrunner.service читає cmds/pending.json кожні 5 секунд

## Workflow
Усе через GitHub: коміт у main → за хвилину сервер оновиться.
Руками до сервера не лізьмо.

## Структура
- bot.py — Telegram бот з Claude AI
- cmd_runner.py — git relay (виконує команди з cmds/pending.json)
- cmds/pending.json — черга команд
- cmds/result.json — результати виконання

## Користувач
Говорить українською, не програміст — пояснювати простими словами.
