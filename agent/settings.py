from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str
    langsmith_api_key: str
    pinecone_api_key: str
    tavily_api_key: str
    
    langsmith_project: str
    langsmith_endpoint: str = "https://api.smith.langchain.com"
    langsmith_tracing: bool = True
    collection_name: str = "lundbeck-docs"
    chroma_persist_directory: str = ".chroma"

    class Config:
        env_file = ".env"

settings = Settings()