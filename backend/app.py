from flask import Flask, request, jsonify
from agent_handler import process_task

app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    # 接收前端发来的消息
    data = request.json
    message = data.get('message', '')

    # 调用独立的函数处理任务
    response = process_task(message)

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

