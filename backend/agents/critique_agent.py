from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel
from tavily import TavilyClient
import os
from langchain_core.messages import SystemMessage, HumanMessage

from dotenv import load_dotenv
load_dotenv()

class Queries(BaseModel):
    queries: list[str]

MODEL = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
TAVILY = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])
RESEARCH_CRITIQUE_PROMPT = ("你是一名研究员，负责提供可以用于修订的相关信息（详见下文）。"
                                        "请生成两条搜索查询，以收集任何相关的信息。"
                                        "最多生成两条查询。"
                                        "请确保所有输出内容都用中文表述，并且要尽量详细和具体。"
                                        )
def research_critique_node(state):
    queries = MODEL.with_structured_output(Queries).invoke([
        SystemMessage(content=RESEARCH_CRITIQUE_PROMPT),
        HumanMessage(content=state['critique'])
    ])
    content = state.get('content', [])
    for q in queries.queries:
        response = TAVILY.search(query=q, max_results=2)
        for r in response['results']:
            content.append(r['content'])
    return {"content": content, "lnode": "research_critique", "count": 1}


# 假设这段代码和 research_critique_node 定义在同一个文件中

def test_research_critique_node():
    # 创建一个模拟状态，包含 'critique' 项
    test_state = {
        'critique': '文章缺乏深度分析，需要增加更多关于人工智能对就业影响的具体数据和案例。'
    }

    # 调用 research_critique_node 函数
    result = research_critique_node(test_state)

    # 打印返回结果
    print("Test Result:", result)


# 执行测试函数
if __name__ == "__main__":
    test_research_critique_node()
