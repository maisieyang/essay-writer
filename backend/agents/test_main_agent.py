from main_agent import ewriter 

from dotenv import load_dotenv
load_dotenv()


def test_full_workflow():
    # 初始化 ewriter 实例
    writer = ewriter()
    
    # 定义初始状态
    initial_state = {
        "task": "研究人工智能对社会的影响",
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
    for state in writer.graph.stream(initial_state, {"configurable": {"thread_id": "1"}}):
        print("当前状态:", state)  # 输出每个状态

    # # 验证最终状态
    # final_state = state
    # assert final_state["planner"] != "", "Draft should not be empty"
    # print("test_full_workflow passed!")


# 运行测试
if __name__ == "__main__":
    test_full_workflow()
