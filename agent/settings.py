from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str
    pinecone_api_key: str
    tavily_api_key: str
    
    collection_name: str = "lundbeck-docs"
    chroma_persist_directory: str = ".chroma"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()