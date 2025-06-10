from langchain_core.messages import ToolMessage
from langgraph.store.base import BaseStore

from agent.state import State
from agent.tools import upsert_memory

async def store_memory_node(state: State, *, store: BaseStore):
    last_message = state.messages[-1]
    memory_tool_call = next((tc for tc in last_message.tool_calls if tc["name"] == "upsert_memory"), None)

    if memory_tool_call:
        args = memory_tool_call["args"]
        result = await upsert_memory.ainvoke({**args, "store": store})
        memory_message = ToolMessage(content=result, tool_call_id=memory_tool_call["id"])
        
        return {"messages": [memory_message]}
    else:
        return {"messages": []}