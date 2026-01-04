import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
    
    AZURE_SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    AZURE_SEARCH_KEY = os.getenv("AZURE_SEARCH_API_KEY")
    AZURE_SEARCH_INDEX = os.getenv("AZURE_SEARCH_INDEX_NAME")

    @classmethod
    def validate(cls):
        missing = []
        for attr in ["AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT", "AZURE_SEARCH_ENDPOINT", "AZURE_SEARCH_KEY", "AZURE_SEARCH_INDEX"]:
            if not getattr(cls, attr):
                missing.append(attr)
        if missing:
            raise ValueError(f"Missing environment variables: {', '.join(missing)}")

    @classmethod
    def llm_config(cls):
        return {
            "config_list": [{
                "model": "gpt-4", # Assumes gpt-4 deployment name is 'gpt-4' or similar. Adjust as needed.
                "api_type": "azure",
                "api_key": cls.AZURE_OPENAI_API_KEY,
                "base_url": cls.AZURE_OPENAI_ENDPOINT,
                "api_version": cls.AZURE_OPENAI_API_VERSION,
            }],
            "temperature": 0,
        }
