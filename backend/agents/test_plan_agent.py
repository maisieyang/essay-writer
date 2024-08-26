from plan_agent import PlanAgent
from typing import TypedDict

from dotenv import load_dotenv
load_dotenv()


class AgentState(TypedDict): 
    task: str
    lnode: str
    plan: str
    count: int

def test_plan_agent():
    agent = PlanAgent()
    
    state = AgentState(
        task="What is the impact of AI on society?",
        lnode="",
        plan="",
        count=0
    )
    
    new_state = agent.run(state)
    print("\nPlan Output:\n")
    print(new_state["plan"])

    
    assert new_state["plan"] != "", "Plan should not be empty"
    assert new_state["lnode"] == "planner", "lnode should be set to 'planner'"
    print("test_plan_agent passed!")




if __name__ == "__main__":
    test_plan_agent()
