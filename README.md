# Azure Agentic RAG Foundry

![Azure Agentic RAG Foundry Hero](assets/hero.png)

## Overview

**Azure Agentic RAG Foundry** is a production-ready, multi-agent system designed to leverage the power of **Microsoft Azure AI Search** and **AutoGen**. This project demonstrates how to orchestrate a team of AI agents to retrieve internal knowledge, synthesize strategic insights, and deliver high-quality reports.

The system mimics a "Corporate Intelligence Unit" where distinct specialized agents collaborate to solve complex queries.

## Architecture & Workflow

The system is built on a modular architecture:

```mermaid
graph TD
    User[User] -->|Query| Manager[Group Chat Manager]
    Manager -->|Orchestrates| Archivist
    Manager -->|Orchestrates| Analyst
    Manager -->|Orchestrates| Critic
    
    subgraph "Agent Swarm"
    Archivist["Archivist Agent<br/>(Retriever)"]
    Analyst["Analyst Agent<br/>(Synthesizer)"]
    Critic["Critic Agent<br/>(Quality Control)"]
    end
    
    Archivist -->|Tools| AISearch[Azure AI Search]
    AISearch -->|Documents| Archivist
    
    style User fill:#f9f,stroke:#333,stroke-width:2px
    style Manager fill:#bbf,stroke:#333,stroke-width:2px
    style AISearch fill:#bfb,stroke:#333,stroke-width:2px
```

### Agent Roles

1.  **The Archivist**: Specialized in information retrieval. It has exclusive access to the `search_knowledge_base` tool, allowing it to query the Azure AI Search index for relevant documents.
2.  **The Analyst**: A strategic thinker who takes raw data snippets from the Archivist and synthesizes them into a coherent narrative.
3.  **The Critic**: Ensures the final output is accurate, grounded in the retrieved data, and logically sound.

## Features

*   **Multi-Agent Orchestration**: Uses Microsoft `pyautogen` for robust agent interaction.
*   **RAG Integration**: Direct integration with Azure AI Search for enterprise-grade retrieval.
*   **Production Ready**: Includes configuration management, environment variable handling, and scalable directory structure.
*   **Extensible**: Easily add new agents or tools to the swarm.

## Getting Started

### Prerequisites

*   Python 3.9+
*   Azure OpenAI Service Resource
*   Azure AI Search Resource

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/YOUR_USERNAME/azure-agentic-rag-foundry.git
    cd azure-agentic-rag-foundry
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Configure environment:
    *   Copy `.env.example` to `.env`.
    *   Fill in your Azure credentials.

    ```bash
    cp .env.example .env
    ```

### Usage

Run the main orchestrator:

```bash
python main.py
```

## Customization

*   **Agents**: Modify `src/agents/definitions.py` to change system prompts or add new agents.
*   **Tools**: Add new tools in `src/tools/` and register them in the agent definitions.

## License

MIT
