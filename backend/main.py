from agents.state_graph import build_state_graph
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    # 构建状态图
    graph = build_state_graph()

    # 定义初始状态
    initial_state = {
        "task": "Write an article about Python",
        "revision_number": 0,
        "max_revisions": 3
    }

    # 运行状态图
    events = graph.stream(initial_state)
    for event in events:
        print(event)