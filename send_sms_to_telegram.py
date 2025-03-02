import os
import requests
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

def send_sms_to_telegram(sms_data):
    # Получаем токен бота и ID чата из переменных окружения
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    # Проверим, что переменные окружения загружены
    print(f"Bot Token: {bot_token}")
    print(f"Chat ID: {chat_id}")

    # Формируем сообщение для Telegram
    message = f"New SMS received:\nSender: {sms_data['sender']}\nMessage: {sms_data['message']}"

    # URL для отправки сообщения в Telegram
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    # Параметры запроса
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    # Отправляем запрос с использованием json (это гарантирует правильную отправку JSON)
    response = requests.post(url, json=payload)
    
    # Выводим ответ от Telegram API для отладки
    print(response.json())
    
    # Возвращаем ответ от API Telegram
    return response.json()
