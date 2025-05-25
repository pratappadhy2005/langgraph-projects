from typing import TypedDict, List
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o")


class AgentState(TypedDict):
    messages: List[HumanMessage]


def process(state: AgentState) -> AgentState:
    messages = state["messages"]
    response = model.invoke(messages)
    print(f"""AI: {response.content}""")
    return state


graph = StateGraph(AgentState)
graph.add_node("process", process)

graph.add_edge(START, "process")
graph.add_edge("process", END)

agent = graph.compile()


user_input = input("Enter your message: ")
while user_input != "exit":
    result = agent.invoke({"messages": [HumanMessage(content=user_input)]})
    user_input = input("Enter your message: ")
