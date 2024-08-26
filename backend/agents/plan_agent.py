from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

class PlanAgent:
    def __init__(self, model=None):
        self.model = model or ChatOpenAI(model="gpt-3.5-turbo", temperature=1)
        self.PLAN_PROMPT = ("作为一名写作专家，请为一个三段式的简短文章撰写一份高级别的提纲。"
                            "根据用户提供的主题，明确文章的三个主要部分，并为每个部分提供相应的说明或写作建议。"
                            "请用中文回答。 "
                            )
    def run(self, state):
        messages = [
            SystemMessage(content=self.PLAN_PROMPT), 
            HumanMessage(content=state['task'])
        ]
        print("---------------------------PlanAgent Start-----------------------------------")
        print("\n")
        print("PlanAgent 输入:\n", messages)  # 打印输入状态
        response = self.model.invoke(messages)
        print("\n")
        print("PlanAgent 输出:\n", response.content)  # 打印输出状态
        print("---------------------------PlanAgent end-----------------------------------")
        return {"plan": response.content, "lnode": "planner", "count": 1}
