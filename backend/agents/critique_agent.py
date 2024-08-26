from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel
from tavily import TavilyClient
import os
from langchain_core.messages import SystemMessage, HumanMessage

class Queries(BaseModel):
    queries: list[str]

class CritiqueAgent:
    def __init__(self, model=None, tavily_client=None):
        self.model = model or ChatOpenAI(model="gpt-3.5-turbo", temperature=1)
        self.tavily = tavily_client or TavilyClient(api_key=os.environ["TAVILY_API_KEY"])
    
        self.RESEARCH_CRITIQUE_PROMPT = ("你是一名研究员，负责提供可以用于修订的相关信息（详见下文）。"
                                        "请生成两条搜索查询，以收集任何相关的信息。"
                                        "最多生成两条查询。"
                                        "请确保所有输出内容都用中文表述，并且要尽量详细和具体。"
                                        )

    def run(self, state):
        queries = self.model.with_structured_output(Queries).invoke([
            SystemMessage(content=self.RESEARCH_CRITIQUE_PROMPT),
            HumanMessage(content=state['critique'])
        ])
        content = state['content'] or []
        for q in queries.queries:
            response = self.tavily.search(query=q, max_results=2)
            for r in response['results']:
                content.append(r['content'])
        return {"content": content, "lnode": "research_critique", "count": 1}
