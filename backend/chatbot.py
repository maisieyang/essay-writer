# from langchain import LLMChain
# from langgraph import StateGraph

# def get_chat_response(message: str) -> str:
#     # 使用 LangChain 和 LangGraph 处理消息并生成回复
#     # 这是一个简单的示例，你可以根据需要扩展它
#     graph = StateGraph({
#         "message": message,
#         "response": ""
#     })
    
#     def process_message(state):
#         state["response"] = f"你发送的消息是: {state['message']}"
#         return state
    
#     graph.add_node("process_message", process_message)
#     graph.add_edge(graph.START, "process_message")
#     graph.add_edge("process_message", graph.END)
    
#     final_state = graph.run({"message": message})
#     return final_state["response"]
