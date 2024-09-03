from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

from dotenv import load_dotenv
load_dotenv()


MODEL = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
REFLECTION_PROMPT = ("你是一名老师，负责为一篇三段式文章打分。"
                                 "请为用户的提交生成评价和建议。"
                                 "提供详细的建议，包括对文章长度、深度、风格等方面的要求。"
                                 "请用中文回答。")
def reflection_node(state):
    messages = [
        SystemMessage(content=REFLECTION_PROMPT),
        HumanMessage(content=state['draft'])
    ]
    response = MODEL.invoke(messages)
    return {"critique": response.content, "lnode": "reflect", "count": 1}



# 假设这段代码和 reflection_node 定义在同一个文件中

def test_reflection_node():
    # 创建一个模拟状态，包含一个 'draft' 项
    test_state = {
        'draft': '这是一个测试的文章草稿，主要讨论了人工智能对未来社会的影响。'
    }

    # 调用 reflection_node 函数
    result = reflection_node(test_state)

    # 打印返回结果
    print("Test Result:", result)

# 执行测试函数
if __name__ == "__main__":
    test_reflection_node()
