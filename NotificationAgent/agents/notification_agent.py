from langgraph.graph import StateGraph
from agents.utils import get_connection_string, get_llm, get_sql_database_toolkit
from langgraph.prebuilt import create_react_agent
from tools.email import individual_email_tool
from tools.telegram import send_notif
from tools.websearch import web_search

connection_string = get_connection_string()
llm = get_llm()
sql_toolkit = get_sql_database_toolkit(llm=llm)
email_tool = individual_email_tool
telegram_tool = send_notif

agent = create_react_agent(
    model=llm,
    tools= sql_toolkit.get_tools() + [web_search, email_tool, telegram_tool]
)