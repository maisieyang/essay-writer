from .plan_agent import plan_node
from .research_agent import research_plan_node
from .generation_agent import generation_node
from .reflection_agent import reflection_node
from .critique_agent import research_critique_node


from langgraph.graph import StateGraph, END
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3
from typing import TypedDict, Annotated, List
import operator
from langchain_core.pydantic_v1 import BaseModel



class AgentState(TypedDict):
    task: str
    lnode: str
    plan: str
    draft: str
    critique: str
    content: List[str]
    queries: List[str]
    revision_number: int
    max_revisions: int
    count: Annotated[int, operator.add]
    configurable: dict


class Queries(BaseModel):
    queries: List[str]



def should_continue(state):
    if state["revision_number"] > state["max_revisions"]:
        return END
    return "reflect"


def build_state_graph():
    builder = StateGraph(AgentState)
    builder.add_node("planner", plan_node)
    builder.add_node("research_plan", research_plan_node)
    builder.add_node("generate", generation_node)
    builder.add_node("reflect", reflection_node)
    builder.add_node("research_critique", research_critique_node)
    builder.set_entry_point("planner")
    builder.add_conditional_edges(
        "generate", 
        should_continue, 
        {"END": END, "reflect": "reflect"}
    )
    builder.add_edge("planner", "research_plan")
    builder.add_edge("research_plan", "generate")
    builder.add_edge("reflect", "research_critique")
    builder.add_edge("research_critique", "generate")

    memory = SqliteSaver(conn=sqlite3.connect(":memory:", check_same_thread=False))


    return builder.compile(

        )


def test_build_state_graph():
    # 调用 build_state_graph 函数，生成状态图
    state_graph = build_state_graph()

    # 创建一个初始状态
    initial_state = {
        "task": "撰写一篇关于人工智能对未来社会影响的文章",
        "lnode": "planner",
        "plan": "",
        "draft": "",
        "critique": "",
        "content": [],
        "queries": [],
        "revision_number": 0,
        "max_revisions": 1,
        "count": 0
    }

    # 模拟运行状态图
    try:
        # 运行状态图
        events = state_graph.stream(initial_state)
        for event in events:
            print(event)
        print("State graph executed successfully.")
    except Exception as e:
        print(f"Error during state graph execution: {e}")

# 执行测试函数
if __name__ == "__main__":
    test_build_state_graph()
