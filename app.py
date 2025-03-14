from flask import Flask, request, jsonify
from send_sms_to_telegram import send_sms_to_telegram

app = Flask(__name__)

# Этот маршрут должен обрабатывать POST-запросы на /sms
@app.route('/sms', methods=['POST'])
def receive_sms():
    data = request.get_json()  # Получаем данные JSON из POST-запроса
    if not data or 'sender' not in data or 'message' not in data:
        return jsonify({"error": "Invalid data"}), 400

    # Отправляем полученные данные в Telegram
    response = send_sms_to_telegram(data)
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
