import streamlit as st
import pandas as pd
from llm_agent import ask_sql_agent

# Streamlit UI Setup
st.set_page_config(page_title="SQLite LLM SQL Agent", layout="wide")
st.title("💬 SQLite SQL Chatbot")

# Sidebar for API Key input
st.sidebar.header("🔑 API Key Configuration")
api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")

st.write("Ask questions about your SQLite database in natural language, and the agent will generate SQL queries and fetch results.")

# User input for query
query = st.text_input("Ask a question about your database:")

if query:
    if not api_key:
        st.warning("⚠️ Please enter your OpenAI API Key in the sidebar.")
    else:
        with st.spinner("Generating SQL query..."):
            response = ask_sql_agent(api_key, query)
            if isinstance(response, pd.DataFrame):
                st.dataframe(response)  # Show table results
            else:
                st.write(response)  # Show text results

# Footer
st.markdown("---")
st.markdown("🔍 Powered by LangChain + OpenAI + Streamlit")
