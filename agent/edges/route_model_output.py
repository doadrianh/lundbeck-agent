from typing import Literal

from langchain_core.messages import AIMessage

from agent.state import State


def route_model_output(state: State) -> Literal["__end__", "human_approval", "tools"]:
    """Determine the next node based on the model's output."""
    last_message = state.messages[-1]
    if not isinstance(last_message, AIMessage):
        raise ValueError(
            f"Expected AIMessage in output edges, but got {type(last_message).__name__}"
        )
    if not last_message.tool_calls:
        return "__end__"
    
    if any([tc["name"] == "upsert_memory" for tc in last_message.tool_calls]):
        return "human_approval"
    else:
        return "tools"