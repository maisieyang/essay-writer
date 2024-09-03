from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel
from tavily import TavilyClient
import os
from langchain_core.messages import SystemMessage, HumanMessage
from typing import List

from dotenv import load_dotenv
load_dotenv()

class Queries(BaseModel):
    queries: List[str]

MODEL = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
TAVILY = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])
RESEARCH_PLAN_PROMPT = ("作为一名研究员，你的任务是为以下文章提供有用的信息。 "
                                     "请生成三条搜索查询，帮助收集与主题相关的重要信息。 "
                                     "最多生成三条搜索查询。")
def research_plan_node(state):
    queries = MODEL.with_structured_output(Queries).invoke([
        SystemMessage(content=RESEARCH_PLAN_PROMPT),
        HumanMessage(content=state['task'])
    ])
    content = state.get('content', [])  # 获取内容，若无则初始化为空列表
    for q in queries.queries:
        response = TAVILY.search(query=q, max_results=2)
        for r in response['results']:
            content.append(r['content'])
    return {"content": content, "queries": queries.queries, "lnode": "research_plan", "count": 1}

# 假设这段代码和 research_plan_node 定义在同一个文件中

def test_research_plan_node():
    # 创建一个模拟状态，包含一个 'task' 项
    test_state = {
        'task': '研究人工智能对未来社会的影响'
    }

    # 调用 research_plan_node 函数
    result = research_plan_node(test_state)

    # 打印返回结果
    print("Test Result:", result)

# 执行测试函数
if __name__ == "__main__":
    test_research_plan_node()
