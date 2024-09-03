from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

from dotenv import load_dotenv
load_dotenv()

MODEL = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
PLAN_PROMPT = ("作为一名写作专家，请为一个三段式的简短文章撰写一份高级别的提纲。"
                "根据用户提供的主题，明确文章的三个主要部分，并为每个部分提供相应的说明或写作建议。"
                "请用中文回答。 "
             )
def plan_node(state):
    messages = [
        SystemMessage(content=PLAN_PROMPT), 
        HumanMessage(content=state['task'])
    ]
    print("---------------------------PlanAgent Start-----------------------------------")
    print("\n")
    response = MODEL.invoke(messages)
    print("PlanAgent 输出:\n", response.content)  # 打印输出状态
    print("---------------------------PlanAgent end-----------------------------------\n")
    return {"plan": response.content, "lnode": "planner", "count": 1}



# 假设这段代码和 plan_node 定义在同一个文件中

def test_plan_node():
    # 创建一个模拟状态，包含一个'task'项
    test_state = {
        'task': '探讨人工智能对未来工作的影响'
    }

    # 调用 plan_node 函数
    result = plan_node(test_state)

    # 打印返回结果
    print("Test Result:", result)

# 执行测试函数
if __name__ == "__main__":
    test_plan_node()
