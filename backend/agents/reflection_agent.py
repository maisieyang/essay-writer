from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

class ReflectionAgent:
    def __init__(self, model=None):
        self.model = model or ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        self.REFLECTION_PROMPT = ("你是一名老师，负责为一篇三段式文章打分。"
                                 "请为用户的提交生成评价和建议。"
                                 "提供详细的建议，包括对文章长度、深度、风格等方面的要求。"
                                 "请用中文回答。")

    
    def run(self, state):
        messages = [
            SystemMessage(content=self.REFLECTION_PROMPT), 
            HumanMessage(content=state['draft'])
        ]
        response = self.model.invoke(messages)
        return {"critique": response.content, "lnode": "reflect", "count": 1}
