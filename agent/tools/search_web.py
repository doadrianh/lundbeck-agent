from typing import Any, cast

from langchain_core.tools import tool
from langchain_tavily import TavilySearch

from agent.configuration import Configuration


@tool
async def search_web(query: str) -> list[str]:
    """Search for general web results.

    This function performs a search using the Tavily search engine, which is designed
    to provide comprehensive, accurate, and trusted results. It's particularly useful
    for answering questions about current events.
    """
    configuration = Configuration.from_context()
    wrapped = TavilySearch(max_results=configuration.max_search_results)
    results = cast(dict[str, Any], await wrapped.ainvoke({"query": query}))
    
    if not results.get("results"):
        return ["No search results found."]
    
    formatted_results = []
    for i, item in enumerate(results["results"], 1):
        result_text = f"""Result {i}:
Title: {item.get('title', 'N/A')}
Content: {item.get('content', 'N/A')}
URL: {item.get('url', 'N/A')}
Relevance Score: {item.get('score', 'N/A')}"""
        formatted_results.append(result_text)
    
    return formatted_results
