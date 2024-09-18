import openai
from src.utils import get_openai_api_key, logger
from config import config

openai.api_key = get_openai_api_key()

def analyze_sentiment(text):
    try:
        response = openai.Completion.create(
            engine=config.GPT_ENGINE,
            prompt=config.PROMPT_TEMPLATE.format(text=text),
            max_tokens=50
        )
        return response.choices[0].text.strip()
    except Exception as e:
        logger.error(f"Error in analyzing sentiment: {e}")
        return "Error"
