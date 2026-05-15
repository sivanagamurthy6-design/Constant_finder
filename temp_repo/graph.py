from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph,START, END
from llm import get_llm


class ChatState(TypedDict):
    messages: Annotated[list, add_messages]
    print(add_messages," inside ChatState")
def chatbot(state:ChatState):
    llm = get_llm()
    response = llm.invoke(state["messages"])
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------Response from LLM:", response)
    print("*****************************************************************************************************************************************************Current messages in state:", state["messages"])
    return {"messages": state["messages"] + [response]}

def build_graph():
    graph = StateGraph(ChatState)
    
    graph.add_node("chatbot", chatbot)
    print("Added chatbot node to graph")
    graph.add_edge(START, "chatbot")
    graph.add_edge("chatbot", END)

    return graph.compile()
# if __name__ == "__main__":
#     graph = build_graph()
#     result = graph.invoke(
#         {"messages": ["Hello, how are you?"]}
#     )
#     print(result)
#     print("Final messages:", result["messages"])
