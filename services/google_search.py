import os
import requests
from dotenv import load_dotenv

load_dotenv(override=True)

openai_api_key = os.getenv('OPENAI_API_KEY')
google_search_key = os.getenv('GOOGLE_API_KEY')
search_engine_id = os.getenv('SEARCH_ENGINE_CX_ID')

def google_search_wikipedia(query):
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query + " site:wikipedia.org",
        "key": google_search_key,
        "cx": search_engine_id,
        "num": 1  # Get only the top result
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "items" in data:
        first_link = data["items"][0]["link"]
        if "wikipedia.org/wiki/" in first_link:  # Ensure it's a Wikipedia article
            return first_link
    return None
