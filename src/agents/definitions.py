import autogen
from src.config import Config
from src.tools.rag import search_knowledge_base

def create_agents():
    llm_config = Config.llm_config()

    # 1. User Proxy - acts as the project manager/user
    user_proxy = autogen.UserProxyAgent(
        name="User_Proxy",
        system_message="A human admin.",
        code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
        human_input_mode="TERMINATE"
    )

    # 2. The Archivist - has access to the search tool
    archivist = autogen.AssistantAgent(
        name="Archivist",
        system_message="""You are the Archivist. Your role is to retrieve information from the knowledge base using the 'search_knowledge_base' tool. 
        When asked a question, use the tool to find answers. 
        Only answer based on the retrieved information. If you cannot find it, state that clearly.""",
        llm_config=llm_config,
    )
    
    # Register the tool
    autogen.agentchat.register_function(
        search_knowledge_base,
        caller=archivist,
        executor=user_proxy,
        name="search_knowledge_base",
        description="Searches the internal knowledge base for documents."
    )

    # 3. The Analyst - synthesizes information
    analyst = autogen.AssistantAgent(
        name="Analyst",
        system_message="""You are the Senior Analyst. You take the raw information provided by the Archivist and synthesize it into a clear, strategic answer. 
        Do not make up facts. Cite sources if available from the Archivist's output.""",
        llm_config=llm_config,
    )
    
    # 4. The Critic - reviews the output
    critic = autogen.AssistantAgent(
         name="Critic",
         system_message="""Critic. Double check plan, claims, code from other agents and provide feedback. 
         Check specificall if the information citation is correct.""",
         llm_config=llm_config,
    )

    return user_proxy, archivist, analyst, critic
