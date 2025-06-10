import uuid
from typing import Annotated, Optional

from langchain_core.tools import InjectedToolArg, tool
from langgraph.store.base import BaseStore

from agent.configuration import Configuration

@tool
async def upsert_memory(
    content: str,
    context: str,
    *,
    memory_id: Optional[uuid.UUID] = None,
    store: Annotated[BaseStore, InjectedToolArg],
):
    """Store all preferences, personal details, and important information unique to the user.

    Use this to remember anything the user shares about themselves that should persist across conversations.
    
    Args:
        content: What to remember about the user
        context: When/where this information came up  
        memory_id: Only provide when updating existing information
    """
    
    mem_id = memory_id or uuid.uuid4()
    user_id = Configuration.from_context().thread_id

    await store.aput(
        ("memories", user_id),
        key=str(mem_id),
        value={"content": content, "context": context},
    )
    return f"Stored memory {mem_id}"