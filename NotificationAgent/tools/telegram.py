from urllib import request
from langchain_core.tools import tool
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
import os
from dotenv import load_dotenv
import urllib
load_dotenv()

@tool("telegram_notif", parse_docstring= True, return_direct = True)
def send_notif(postUrl:str) -> str:
    """Sends an url to the telegram channel whose chat id is specified

    Args:
    postUrl: Url of the post from directai.blog to be shared to telegram group
    """
    url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/sendMessage?chat_id={os.getenv('TELEGRAM_CHATID')
                                                                                           }&text={urllib.parse.quote_plus(postUrl)}"
    response = request.get(url)
    return response
