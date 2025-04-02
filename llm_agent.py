import streamlit as st
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain.sql_database import SQLDatabase
from langchain.chat_models import ChatOpenAI
from sqlalchemy import create_engine

# SQLite database file
DB_PATH = "sqlite:///sample.db"
engine = create_engine(DB_PATH)
db = SQLDatabase(engine)


def get_sql_agent(api_key: str):
    """Creates an LLM-powered SQL Agent using the user's OpenAI API key."""
    llm = ChatOpenAI(model_name="gpt-4o-mini",
                     temperature=0, openai_api_key=api_key)
    return create_sql_agent(
        llm=llm,
        db=db,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )


def ask_sql_agent(api_key: str, query: str):
    """Executes an LLM-generated SQL query."""
    if not api_key:
        return "❌ Please enter a valid OpenAI API Key."

    sql_agent = get_sql_agent(api_key)
    try:
        return sql_agent.run(query)
    except Exception as e:
        return f"Error: {e}"
