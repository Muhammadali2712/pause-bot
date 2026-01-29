import os
import asyncio
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_CHAT_ID = "-5214164660"  # ← ЗАМЕНИТЕ НА СВОЙ ID!

async def main():
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN не установлен!")
        return

    bot = Bot(token=BOT_TOKEN)
    try:
        # Проверка доступа к группе
        await bot.send_message(
            chat_id=GROUP_CHAT_ID,
            text="✅ Бот работает. Ожидание сообщений от @in_siderpay_bot..."
        )
        print("✅ Бот может писать в группу")
    except Exception as e:
        print(f"❌ Ошибка при отправке тестового сообщения: {e}")
        return

    # Проверка последних сообщений
    try:
        updates = await bot.get_updates(limit=5, timeout=15)
        for update in reversed(updates):
            msg = update.message
            if msg and str(msg.chat.id) == GROUP_CHAT_ID:
                if msg.from_user and msg.from_user.username == "gushtbiryon":
                    await bot.send_message(
                        chat_id=GROUP_CHAT_ID,
                        text="Ставьте на паузу пожалуйста",
                        reply_to_message_id=msg.message_id
                    )
                    print(f"✅ Ответили на сообщение #{msg.message_id}")
                    return
        print("ℹ️ Нет новых сообщений от @in_siderpay_bot")
    except Exception as e:
        print(f"❌ Ошибка при чтении сообщений: {e}")

if __name__ == "__main__":
    asyncio.run(main())
