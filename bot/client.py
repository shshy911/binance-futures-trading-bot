from binance.client import Client
import logging
import os
logger = logging.getLogger(name=__name__)
from dotenv import load_dotenv
def get_client():
    load_dotenv()
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    if api_key is None:
        logger.error("ValueError: API Key missing")
        raise ValueError("API Key missing")
    if api_secret is None:
        logger.error("ValueError:API Secret missing")
        raise ValueError("API Secret missing")
    client = Client(api_key=api_key,api_secret=api_secret,testnet=True)
    logger.info("Client Created")
    return client