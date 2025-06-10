
from langgraph.prebuilt import ToolNode
from agent.tools import search_drug, search_lundbeck, search_web

tools_node = ToolNode([search_drug, search_lundbeck, search_web])
