from  ..critique_agent import CritiqueAgent
from typing import TypedDict, List

from dotenv import load_dotenv
load_dotenv()

class AgentState(TypedDict):
    task: str
    lnode: str
    critique: str
    content: List[str]
    queries: List[str]
    count: int

def format_and_print(text_list):
    for text in text_list:
        # 使用换行符分隔字符串，并逐行打印
        formatted_text = text.split("\n")
        for line in formatted_text:
            print(line)
        print()  # 每个段落之后插入一个空行

def test_critique_agent():
    agent = CritiqueAgent()
    
    state = AgentState(
        task="What is the impact of AI on society?",
        lnode="",
        critique="This is a critique.",
        content=[],
        queries=[],
        count=0
    )
    
    new_state = agent.run(state)

    print("\nPlan Output:\n")

    format_and_print(new_state["content"])
    
    assert "content" in new_state, "Content should be updated"
    assert new_state["lnode"] == "research_critique", "lnode should be set to 'research_critique'"
    print("test_critique_agent passed!")


if __name__ == "__main__":
    test_critique_agent()
