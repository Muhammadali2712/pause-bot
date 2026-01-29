import os
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_CHAT_ID = "-5214164660"

if not BOT_TOKEN:
    print("❌ BOT_TOKEN не установлен!")
else:
    bot = Bot(token=BOT_TOKEN)
    try:
        bot.send_message(chat_id=GROUP_CHAT_ID, text="✅ Тестовый сигнал")
        print("✅ Бот может писать в группу")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
