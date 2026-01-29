import os
import asyncio
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_CHAT_ID = "-5214164660"  # ← Ваш ID группы
TARGET_BOT_USERNAME = "gushtbiryon"  # ← Username без @

async def main():
    if not BOT_TOKEN:
        print("❌ Ошибка: BOT_TOKEN не установлен!")
        return

    bot = Bot(token=BOT_TOKEN)
    
    try:
        # Проверяем, может ли бот писать в группу
        await bot.send_message(
            chat_id=GROUP_CHAT_ID,
            text="✅ Бот активен. Следит за сообщениями от @" + TARGET_BOT_USERNAME
        )
        print("✅ Подключение к группе успешно")
    except Exception as e:
        print(f"❌ Не могу отправить сообщение в группу: {e}")
        return

    try:
        # Получаем последние 5 сообщений
        updates = await bot.get_updates(limit=5, timeout=15)
        for update in reversed(updates):
            msg = update.message
            if msg and str(msg.chat.id) == GROUP_CHAT_ID:
                if msg.from_user and msg.from_user.username == TARGET_BOT_USERNAME:
                    # Отвечаем только если ещё не отвечали
                    if not msg.reply_to_message:
                        await bot.send_message(
                            chat_id=GROUP_CHAT_ID,
                            text="Ставьте на паузу пожалуйста",
                            reply_to_message_id=msg.message_id
                        )
                        print(f"✅ Ответили на сообщение от @{TARGET_BOT_USERNAME} (ID: {msg.message_id})")
                        return
        print(f"ℹ️ Нет новых сообщений от @{TARGET_BOT_USERNAME}")
    except Exception as e:
        print(f"❌ Ошибка при проверке сообщений: {e}")

if __name__ == "__main__":
    asyncio.run(main())
