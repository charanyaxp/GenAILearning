from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_tavily import TavilySearch
load_dotenv()

@tool("web_search", parse_docstring= True, return_direct = True)
def web_search() -> None:
    """Used to look for new updates in the directai.blog.
       When there is latest post, the url is shared with the students through Telegram chat
    """
    tavily_tool = TavilySearch(
    max_results=5,
    topic="general",
    # include_answer=False,
    # include_raw_content=False,
    # include_images=False,
    # include_image_descriptions=False,
    # search_depth="basic",
    # time_range="day",
    include_domains=["directai.blog"],
    # exclude_domains=None
)
