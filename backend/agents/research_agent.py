from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel
from tavily import TavilyClient
import os
from langchain_core.messages import SystemMessage, HumanMessage

class Queries(BaseModel):
    queries: list[str]

class ResearchAgent:
    def __init__(self, model=None, tavily_client=None):
        self.model = model or ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        self.tavily = tavily_client or TavilyClient(api_key=os.environ["TAVILY_API_KEY"])
        self.RESEARCH_PLAN_PROMPT = ("作为一名研究员，你的任务是为以下文章提供有用的信息。 "
                                     "请生成三条搜索查询，帮助收集与主题相关的重要信息。 "
                                     "最多生成三条搜索查询。")
    
    def run(self, state):
        queries = self.model.with_structured_output(Queries).invoke([
            SystemMessage(content=self.RESEARCH_PLAN_PROMPT),
            HumanMessage(content=state['task'])
        ])
        content = state['content'] or []  # add to content
        for q in queries.queries:
            response = self.tavily.search(query=q, max_results=2)
            for r in response['results']:
                content.append(r['content'])
        return {"content": content, "queries": queries.queries, "lnode": "research_plan", "count": 1}
