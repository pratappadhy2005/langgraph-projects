from typing import TypedDict
from langgraph.graph import StateGraph


class PersonalisedAgent(TypedDict):
    name: str


def trigger_personlised_mesage(state: PersonalisedAgent) -> PersonalisedAgent:
    state['name'] = state['name'] + \
        " , you are doing an amazing job learning LangGraph?"
    return state


graph = StateGraph(PersonalisedAgent).add_node(
    "personalised_message", trigger_personlised_mesage)

graph.set_entry_point("personalised_message")
graph.set_finish_point("personalised_message")

app = graph.compile()

result = app.invoke({"name": "Bob"})

print(result["name"])
