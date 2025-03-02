import os
from dotenv import load_dotenv
import requests

# Загрузка переменных из .env файла
load_dotenv()

# Функция для отправки SMS в Telegram
def send_sms_to_telegram(sms_data):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    
    # Формируем сообщение для Telegram
    message = f"New SMS received:\nSender: {sms_data['sender']}\nMessage: {sms_data['message']}"
    
    # URL API Telegram
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    # Параметры запроса
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    
    # Отправляем POST-запрос на API Telegram
    response = requests.post(url, data=payload)
    
    # Возвращаем ответ от Telegram API
    return response.json()
