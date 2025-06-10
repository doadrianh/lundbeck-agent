from datetime import UTC, datetime
from typing import Dict, List, cast

from langchain_core.messages import AIMessage, SystemMessage
from langgraph.store.base import BaseStore

from agent.configuration import Configuration
from agent.state import State
from agent.tools import TOOLS
from agent.utils import load_chat_model


async def call_model_node(state: State, store: BaseStore) -> Dict[str, List[AIMessage]]:
    """Call the LLM powering our "agent"."""
    configuration = Configuration.from_context()

    model = load_chat_model(configuration.model).bind_tools(TOOLS)

    memories = await store.asearch(
        ("memories", configuration.thread_id),
        query=str([m.content for m in state.messages[-configuration.max_history_messages:]]),
        limit=10,
    )

    memories_formatted = "\n".join(f"[{mem.key}]: {mem.value} (similarity: {mem.score})" for mem in memories)
    if memories_formatted:
        memories_formatted = f"""\n\nMemories:\n{memories_formatted}\n\n"""
        
    system_message = configuration.system_prompt.format(
        system_time=datetime.now(tz=UTC).isoformat(),
        memories=memories_formatted
    )

    selected = []
    for message in reversed(state.messages):
        if len(selected) < configuration.max_history_messages:
            selected.append(message)
        elif isinstance(message, AIMessage):
            selected.append(message)
            break

    messages = [SystemMessage(content=system_message), *state.messages]

    response = cast(AIMessage, await model.ainvoke(messages))
    
    if state.is_last_step and response.tool_calls:
        return {
            "messages": [
                AIMessage(
                    id=response.id,
                    content="Sorry, I could not find an answer to your question in the specified number of steps.",
                )
            ]
        }

    return {"messages": [response]}

