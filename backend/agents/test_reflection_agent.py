from reflection_agent import ReflectionAgent
from typing import TypedDict
from dotenv import load_dotenv
load_dotenv()


class AgentState(TypedDict):
    task: str
    lnode: str
    draft: str
    critique: str
    count: int

def test_reflection_agent():
    agent = ReflectionAgent()
    
    state = AgentState(
        task="What is the impact of AI on society?",
        lnode="",
        draft="This is a draft.",
        critique="",
        count=0
    )
    
    new_state = agent.run(state)

    print("\nPlan Output:\n")
    print(new_state["critique"])
    
    assert new_state["critique"] != "", "Critique should not be empty"
    assert new_state["lnode"] == "reflect", "lnode should be set to 'reflect'"
    print("test_reflection_agent passed!")

if __name__ == "__main__":
    test_reflection_agent()
