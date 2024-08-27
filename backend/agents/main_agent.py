from plan_agent import PlanAgent
from research_agent import ResearchAgent
from writer_agent import WriterAgent
from reflection_agent import ReflectionAgent
from critique_agent import CritiqueAgent
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


class Queries(BaseModel):
    queries: List[str]

class ewriter():
    def __init__(self):
        self.plan_agent = PlanAgent()
        self.research_agent = ResearchAgent()
        self.writer_agent = WriterAgent()
        self.reflection_agent = ReflectionAgent()
        self.critique_agent = CritiqueAgent()

        builder = StateGraph(AgentState)
        builder.add_node("planner", self.plan_agent.run)
        builder.add_node("research_plan", self.research_agent.run)
        builder.add_node("generate", self.writer_agent.run)
        builder.add_node("reflect", self.reflection_agent.run)
        builder.add_node("research_critique", self.critique_agent.run)

        builder.set_entry_point("planner")


        builder.add_conditional_edges(
            "generate", 
            self.should_continue, 
            {END: END, "reflect": "reflect"}
        )

        builder.add_edge("planner", "research_plan")
        builder.add_edge("research_plan", "generate")
        builder.add_edge("reflect", "research_critique")
        builder.add_edge("research_critique", "generate")

        builder.add_edge("generate", END)
        
        memory = SqliteSaver(conn=sqlite3.connect(":memory:", check_same_thread=False))
        self.graph = builder.compile(
            checkpointer=memory,
            interrupt_after=['planner', 'generate', 'reflect', 'research_plan', 'research_critique']
        )


    def should_continue(self, state):
        if state["revision_number"] > state["max_revisions"]:
            return END
        return "reflect"
