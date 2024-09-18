import logging
from config import config

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    return logging.getLogger(__name__)

logger = setup_logging()

def get_openai_api_key():
    return config.OPENAI_API_KEY
