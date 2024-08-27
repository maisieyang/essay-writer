from agents.main_agent import ewriter

def process_task(task):
    # 初始化ewriter实例
    writer = ewriter()

    # 定义初始状态
    initial_state = {
        "task": task,
        "lnode": "",
        "plan": "",
        "draft": "",
        "critique": "",
        "content": [],
        "queries": [],
        "revision_number": 1,
        "max_revisions": 3,
        "count": 0
    }

    # 运行完整的工作流
    final_state = None
    for state in writer.graph.stream(initial_state, {"configurable": {"thread_id": "1"}}):
        final_state = state  # 保存最终状态

    # 返回最终状态中的结果
    if final_state and "draft" in final_state:
        return final_state["draft"]
    else:
        return "任务执行失败或未生成内容。"
