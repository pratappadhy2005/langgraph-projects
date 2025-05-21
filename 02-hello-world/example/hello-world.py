from typing import TypedDict
from langgraph.graph import StateGraph

# We now create AgentState - shared data structure that keeps track of information as your app runs


class MyFirstState(TypedDict):  # Our state schema
    message: str


def greeting_note(state: MyFirstState) -> MyFirstState:
    """Simple node that needs a greeting message in the state."""

    state['message'] = "Hey " + state['message'] + " , how is your day?"
    return state


graph = StateGraph(MyFirstState).add_node("greeter", greeting_note)

graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

app = graph.compile()

result = app.invoke({"message": "Will"})

print(result["message"])
