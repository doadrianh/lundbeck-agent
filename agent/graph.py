from langgraph.graph import StateGraph, START

from agent.configuration import Configuration
from agent.state import InputState, State
from agent.nodes import call_model_node, tools_node, store_memory_node, human_approval_node
from agent.edges import route_model_output

builder = StateGraph(State, input=InputState, config_schema=Configuration)

# Graph Nodes
builder.add_node("call_model", call_model_node)
builder.add_node("tools", tools_node)
builder.add_node("store_memory", store_memory_node)
builder.add_node("human_approval", human_approval_node)

# Graph Edges
builder.add_edge(START, "call_model")
builder.add_conditional_edges("call_model", route_model_output)
builder.add_edge("tools", "call_model")
builder.add_edge("store_memory", "call_model")

graph = builder.compile(name="Lundbeck Agent")