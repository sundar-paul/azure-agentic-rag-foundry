from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from src.config import Config

def search_knowledge_base(query: str) -> str:
    """
    Searches the Azure AI Search index for information related to the query.
    useful for retrieving context about internal documents, policies, or data.
    """
    try:
        credential = AzureKeyCredential(Config.AZURE_SEARCH_KEY)
        client = SearchClient(
             endpoint=Config.AZURE_SEARCH_ENDPOINT,
             index_name=Config.AZURE_SEARCH_INDEX,
             credential=credential
        )
        
        results = client.search(search_text=query, top=3)
        
        output = []
        for result in results:
            # Assuming 'content' field exists, fallback to dumping all fields if not
            content = result.get("content") or str(result)
            source = result.get("source_url") or result.get("filepath") or "Unknown Source"
            output.append(f"Source: {source}\nContent: {content}\n---")
            
        if not output:
            return "No relevant information found in the knowledge base."
            
        return "\n".join(output)
    except Exception as e:
        return f"Error searching knowledge base: {str(e)}"
