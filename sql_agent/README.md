# LLM SQL Chatbot

This project is a **Streamlit** application that allows interaction with a **SQLite** database using an intelligent **SQL agent** powered by **LangChain** and **OpenAI GPT-4o**. The goal is to allow users to make natural language queries to the database and get responses through a chat interface.

## Features

- **Natural Language Interaction**: The chatbot accepts natural language questions and converts them into SQL queries.
- **LangChain Integration**: Uses LangChain to create an SQL agent that automatically generates and executes SQL queries.
- **SQLite Database**: An SQLite database is automatically created with random data for testing the chatbot.
- **User-Friendly Interface with Streamlit**: The frontend is built with Streamlit, providing a simple and effective way for users to interact with the chatbot.

## Project Structure

The project is divided into three main files:

1. **`setup_db.py`**: Creates an SQLite database with random data for testing purposes.
2. **`llm_agent.py`**: Contains the logic for integrating with LangChain and OpenAI API to generate and execute SQL queries.
3. **`app.py`**: The Streamlit user interface for interacting with the chatbot.

## Prerequisites

Before running the project, install the necessary dependencies:

```bash
pip install -r requirements.txt
```

## How to Run the Project

### Step 1: Generate the SQLite Database

Before running the application, you need to generate the SQLite database with random data. Run the following script once to create the database:

```bash
python setup_db.py
```

This script will create the `sample.db` file and populate the database with tables for users and orders, as well as add fake data using the **Faker** library.

### Step 2: Run the Streamlit Application

After generating the database, start the Streamlit app by running the following command:

```bash
streamlit run app.py
```

### Step 3: Access the Interface

Open your browser and visit the URL provided by Streamlit (usually `http://localhost:8501`). From there, you can interact with the chatbot, ask questions about the database, and get SQL query results.

## How It Works

1. The user enters their **OpenAI API key** in the Streamlit sidebar.
2. The chatbot receives a **natural language question** about the SQLite database.
3. **LangChain** uses the API key to generate an SQL query based on the question.
4. The generated SQL query is executed on the database, and the **results are returned** to the user in either a table or text format.

## Example Queries

- **How many users are there in the database?**
- **Show the top 5 best-selling products.**
- **Which orders were made by a specific user?**

## Dependencies

Here are the main libraries used in the project:

- **Streamlit**: For the user interface.
- **LangChain**: To create the SQL agent with OpenAI integration.
- **OpenAI GPT-4**: Used to generate SQL queries from natural language questions.
- **SQLite**: Database used to store sample data.
- **Faker**: Library to generate fake data for testing.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more details.