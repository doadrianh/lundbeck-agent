from typing import Literal
from langchain_core.messages import ToolMessage
from langgraph.types import interrupt, Command

from agent.state import State

def human_approval_node(state: State) -> Command[Literal["__end__", "store_memory"]]:
    confirmation = interrupt(
        {
            "question": "Is it okay to store this in the memory?",
        }
    )

    if confirmation == "yes":
        return Command(goto="store_memory")
    else:
        return Command(update={"messages": [ToolMessage(content="Ignored memoization.", tool_call_id=state.messages[-1].tool_calls[0]["id"])]})


