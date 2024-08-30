from plan_agent import PlanAgent
from research_agent import ResearchAgent
from writer_agent import WriterAgent
from reflection_agent import ReflectionAgent
from critique_agent import CritiqueAgent
from langgraph.graph import StateGraph, END, START
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


class Queries(BaseModel):
    queries: List[str]

class ManagerAgent():
    def __init__(self):
        self.plan_agent = PlanAgent()
        self.research_agent = ResearchAgent()
        self.writer_agent = WriterAgent()


        builder = StateGraph(AgentState)
        builder.add_node("planner", self.plan_agent.run)
        builder.add_node("research", self.research_agent.run)
        builder.add_node("generate", self.writer_agent.run)

        builder.add_edge(START, "planner")
        builder.add_edge("planner", "research")
        builder.add_edge("research", "generate")
        builder.add_edge("generate", END)
        


        self.graph = builder.compile()

from IPython.display import Image, display

try:
    display(Image(graph.get_graph().draw_mermaid_png()))
except Exception:
    # This requires some extra dependencies and is optional
    pass