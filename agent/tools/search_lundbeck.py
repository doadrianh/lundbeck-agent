from langchain_pinecone import PineconeVectorStore
from langchain_core.tools import create_retriever_tool
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone, ServerlessSpec

from agent.settings import settings

pinecone = Pinecone(api_key=settings.pinecone_api_key)

if not pinecone.has_index(settings.collection_name):
    pinecone.create_index(
        name=settings.collection_name,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pinecone.Index(settings.collection_name)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vector_store = PineconeVectorStore(index=index, embedding=embeddings)

search_lundbeck = create_retriever_tool(
    retriever=vector_store.as_retriever(),
    name="search_lundbeck",
    description="Search the Lundbeck knowledge base for information about focus, science, stories, and sustainability.",
)