# Серверный модуль онлайн-сервиса доставки «ВкусВезёт»
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1/menu', methods=['GET'])
def get_menu():
    return jsonify({
        'status': 'success',
        'categories': ['Пицца', 'Готовые рационы', 'Супы', 'Напитки'],
        'items_count': 24
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
