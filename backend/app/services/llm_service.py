import os

from dotenv import load_dotenv
from google import genai

from app.services.sql_service import get_database_schema


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def generate_sql(question: str):

    schema = get_database_schema()

    prompt = f"""
You are an expert SQL developer.

Convert the user's natural language question into
a SQLite SQL query.

Here is the actual database schema:

{schema}

User question:

{question}

Rules:

1. Generate only SQL.
2. Only generate SELECT queries.
3. Never generate INSERT, UPDATE, DELETE, DROP, ALTER, or CREATE.
4. Use only tables and columns that exist in the database.
5. Return only the SQL query.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    sql = response.text.strip()

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")

    return sql.strip()


def correct_sql(question: str, sql: str, error: str):

    schema = get_database_schema()

    prompt = f"""
You are an expert SQLite SQL developer.

The user asked:

{question}

The database schema is:

{schema}

The generated SQL was:

{sql}

The database returned this error:

{error}

Fix the SQL query.

Rules:

1. Return only the corrected SQL query.
2. Only generate SELECT queries.
3. Never generate INSERT, UPDATE, DELETE, DROP, ALTER, or CREATE.
4. Use only tables and columns that exist in the database.
5. Make sure the corrected query answers the user's original question.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    corrected_sql = response.text.strip()

    corrected_sql = corrected_sql.replace("```sql", "")
    corrected_sql = corrected_sql.replace("```", "")

    return corrected_sql.strip()