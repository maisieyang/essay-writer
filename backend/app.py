import time
import logging
from flask import Flask, request, Response
from agent_handler import process_task

app = Flask(__name__)

# 设置日志记录
logging.basicConfig(level=logging.INFO)

def generate_response(message):
    try:
        for response_part in process_task(message):
            yield f"data: {response_part}\n\n"
    except Exception as e:
        logging.error(f"处理任务时出错: {e}")
        yield "data: 处理任务时发生错误。\n\n"

@app.route('/api/chat', methods=['GET'])
def chat():
    message = request.args.get('message', '')
    return Response(generate_response(message), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
