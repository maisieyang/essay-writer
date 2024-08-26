from dotenv import load_dotenv
load_dotenv()


from research_agent import ResearchAgent
from typing import TypedDict, List

class AgentState(TypedDict):
    task: str
    lnode: str
    content: List[str]
    queries: List[str]
    count: int

def test_research_agent():
    agent = ResearchAgent()
    
    state = AgentState(
        task="What is the impact of AI on society?",
        lnode="",
        content=[],
        queries=[],
        count=0
    )
    
    new_state = agent.run(state)

    print("\n Queries Output:\n")
    print(new_state["queries"])

    
    assert "content" in new_state, "Content should be generated"
    assert new_state["content"], "Content should not be empty"
    assert "queries" in new_state, "Queries should be present"
    assert new_state["lnode"] == "research_plan", "lnode should be set to 'research_plan'"
    print("test_research_agent passed!")

if __name__ == "__main__":
    test_research_agent()
