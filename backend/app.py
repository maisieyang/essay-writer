import time
import logging
from flask import Flask, request, jsonify
from agent_handler import process_task

app = Flask(__name__)

# 设置日志记录
logging.basicConfig(level=logging.INFO)

@app.route('/api/chat', methods=['POST'])
def chat():
    # 记录开始时间
    start_time = time.time()
    
    # 接收前端发来的消息
    data = request.json
    message = data.get('message', '')

    # 调用独立的函数处理任务
    try:
        response = process_task(message)
    except Exception as e:
        # 记录异常
        logging.error(f"处理任务时出错: {e}")
        response = "处理任务时发生错误。"

    # 记录结束时间
    end_time = time.time()
    processing_time = end_time - start_time

    # 记录日志
    logging.info(f"请求处理时间: {processing_time:.2f} 秒")

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
