from dotenv import load_dotenv
load_dotenv()

from writer_agent import WriterAgent
from typing import TypedDict, List

class AgentState(TypedDict):
    task: str
    lnode: str
    plan: str
    draft: str
    content: List[str]
    revision_number: int
    count: int

def test_writer_agent():
    agent = WriterAgent()
    
    state = AgentState(
        task="What is the impact of AI on society?",
        lnode="",
        plan="This is a plan.",
        draft="",
        content=["Research content 1", "Research content 2"],
        revision_number=1,
        count=0
    )
    
    new_state = agent.run(state)

    print("\n Writer Output:\n")
    print(new_state["draft"])

    
    assert new_state["draft"] != "", "Draft should not be empty"
    assert new_state["lnode"] == "generate", "lnode should be set to 'generate'"
    print("test_writer_agent passed!")

if __name__ == "__main__":
    test_writer_agent()
