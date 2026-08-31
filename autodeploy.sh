#!/bin/bash
# Автодеплой: щохвилини тягне свіжий код з GitHub і перезапускає бота при змінах.
# ВАЖЛИВО: справжня папка бота — /home/bot/claude-bot (не /root/...).
REPO=/home/bot/claude-bot
cd "$REPO" || exit 1
git config --global --add safe.directory "$REPO" 2>/dev/null
git fetch origin --quiet 2>/dev/null || exit 0
BEFORE=$(git rev-parse HEAD 2>/dev/null)
git reset --hard origin/main --quiet 2>/dev/null
AFTER=$(git rev-parse HEAD 2>/dev/null)
if [ "$BEFORE" != "$AFTER" ]; then
    systemctl restart mybot
    echo "$(date) deployed $AFTER" >> /root/autodeploy.log
fi
