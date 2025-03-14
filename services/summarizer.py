import os
from dotenv import load_dotenv

import openai


from .website_scraper import WikiWebsite

load_dotenv(override=True)

openai_api_key = os.getenv('OPENAI_API_KEY')


SYSTEM_PROMPT = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. \
Respond in markdown."

def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "\nThe contents of this website is as follows; \
please provide a short summary of this website in markdown. \
If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.main_text
    return user_prompt

def messages_for(website):
    return [
                {'role': 'system', 'content': SYSTEM_PROMPT},
                {'role': 'user', 'content': user_prompt_for(website)}
            ]


def summarize(url):
    website = WikiWebsite(url)
    oai = openai.OpenAI()
    response = oai.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages_for(website)
    )
    return response.choices[0].message.content
