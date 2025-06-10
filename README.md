# Lundbeck Agentic Chatbot

An AI-powered patient support chatbot featuring integrated retrieval, memory, ICD-10 database search, and seamless human handoff capabilities.

## Requirements

Build an AI agent for a patient support chatbot with the following features:

- Integration of multiple components: retrieval, language model inference, memory, and agent orchestration.
- Capability to search the ICD-10 database.
- Ability to transfer chats to human agents.
- Implementation of privacy considerations.
- Multi-turn conversation memory capability.
- Front-end user interface.
- Chatbot logging for audit trails.

## Knowledge Base Construction

### Vector Database

The chatbot uses Pinecone as the primary vector database, ingesting content from the company website within the following scopes:

- Our Focus
- Our Science
- Stories
- Sustainability
- About Us

### ICD-10 Drug Dataset

A sample ICD-10 drug dataset was downloaded from a public source and is used as a structured, queryable table with Pandas.

## Achievements

- **Integrated AI Architecture**: Developed a multi-component system combining retrieval, language model inference, memory, and agent orchestration.
- **ICD-10 Database Integration**: Implemented searchable ICD-10 drug database functionality using Pandas for structured queries.
- **Human Handoff**: Enabled seamless chat transfer to human agents when necessary.
- **Privacy & Security**: Incorporated privacy considerations and data protection measures.
- **Conversation Memory**: Deployed multi-turn conversation memory for contextual interactions.
- **Audit & Logging**: Established a comprehensive chatbot logging system using LangSmith.

## Technical Stack

- **Vector Database**: Pinecone for semantic search and retrieval.
- **Knowledge Base**: Company website content across five key areas.
- **Data Processing**: Pandas for ICD-10 dataset management.
- **Memory System**: Multi-turn conversation context retention.

## How to Run the Project Locally

- **Backend**:
  ```bash
  pip install poetry
  poetry env activate
  poetry install
  poetry run langgraph dev
  ```

- **Frontend**:
  ```bash
  npm install
  npm run dev
  ```
