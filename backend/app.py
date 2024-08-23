from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    # 接收前端发来的消息
    data = request.json
    message = data.get('message', '')

    # 返回一个简单的响应
    response = f"Received message: {message}"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

