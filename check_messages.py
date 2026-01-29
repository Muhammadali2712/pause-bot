import os
import asyncio
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_CHAT_ID = "-1001234567890"  # ← ЗАМЕНИТЕ НА СВОЙ ID ПОЗЖЕ def main():
    if not BOT_TOKEN:
        print("Ошибка: BOT_TOKEN не установлен!")
        return

    bot = Bot(token=BOT_TOKEN)
    try:
        # Получаем последние 5 сообщений из группы
        updates = await bot.get_updates(limit=5, timeout=15)
        for update in reversed(updates):
            msg = update.message
            if msg and str(msg.chat.id) == GROUP_CHAT_ID:
                if msg.from_user and msg.from_user.username == "in_siderpay_bot":
                    # Проверяем, нет ли уже ответа на это сообщение
                    if not msg.reply_to_message:
                        await bot.send_message(
                            chat_id=GROUP_CHAT_ID,
                            text="Ставьте на паузу пожалуйста",
                            reply_to_message_id=msg.message_id
                        )
                        print(f"✅ Ответили на сообщение #{msg.message_id}")
                        return
        print("❌ Нет новых сообщений от @in_siderpay_bot")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    asyncio.run(main())
