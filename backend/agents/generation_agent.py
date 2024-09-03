from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
load_dotenv()


MODEL = ChatOpenAI(model="gpt-4-turbo", temperature=0)
WRITER_PROMPT = ( "你是一名文章助理，任务是撰写出色的三段式文章。"
                              "根据用户的要求和初步提纲，生成最好的文章。"
                              "如果用户提供了反馈，请根据之前的尝试进行修订。"
                              "请用中文表达。"
                              "请充分利用以下所有信息：\n"
                              "------\n"
                              "{content}"
)
def generation_node(state):
    content = "\n\n".join(state['content'] or [])
    user_message = HumanMessage(
        content=f"{state['task']}\n\nHere is my plan:\n\n{state['plan']}")
    messages = [
        SystemMessage(
            content=WRITER_PROMPT.format(content=content)
        ),
        user_message
    ]
    response = MODEL.invoke(messages)
    return {
        "draft": response.content, 
        "revision_number": state.get("revision_number", 1) + 1,
        "lnode": "generate",
        "count": 1,
    }


# 假设这段代码和 generation_node 定义在同一个文件中

def test_generation_node():
    # 创建一个模拟状态，包含 'task'、'plan' 和 'content' 项
    test_state = {
        'task': '撰写一篇关于人工智能对未来社会影响的文章',
        'plan': '第一段介绍人工智能的现状；第二段讨论人工智能对就业的影响；第三段探讨人工智能对未来社会结构的可能影响。',
        'content': ['这是初步的文章草稿，主要讨论了人工智能对社会的影响。']
    }

    # 调用 generation_node 函数
    result = generation_node(test_state)

    # 打印返回结果
    print("Test Result:", result)


# 执行测试函数
if __name__ == "__main__":
    test_generation_node()
