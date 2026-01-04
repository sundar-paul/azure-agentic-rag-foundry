import autogen
from src.config import Config
from src.agents.definitions import create_agents
import sys

def main():
    try:
        # Validate environment variables
        # Config.validate() # Commented out to allow running without keys for demo purposes if needed, but best to keep safe.
        pass
    except ValueError as e:
        print(f"Configuration Error: {e}")
        print("Please create a .env file based on .env.example")
        sys.exit(1)

    user_proxy, archivist, analyst, critic = create_agents()

    groupchat = autogen.GroupChat(
        agents=[user_proxy, archivist, analyst, critic], 
        messages=[], 
        max_round=12
    )
    
    manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=Config.llm_config())

    print("Welcome to the Azure Agentic RAG Foundry.")
    print("Initializing agents...")
    
    initial_query = "What is the strategic overview for Q4 based on the internal documents?"
    
    print(f"Initiating chat with query: {initial_query}")
    
    user_proxy.initiate_chat(
        manager,
        message=initial_query
    )

if __name__ == "__main__":
    main()
