import sqlglot
from sqlglot import exp

from sqlalchemy import inspect

from database.connection import engine


def validate_sql(sql: str):
    try:
        statements = sqlglot.parse(sql)

        if len(statements) != 1:
            return False, "Only one SQL statement is allowed."

        statement = statements[0]

        if not isinstance(statement, exp.Query):
            return False, "Only SELECT queries are allowed."

        return True, "SQL is valid."

    except Exception as e:
        return False, f"Invalid SQL: {str(e)}"


def get_database_schema():
    inspector = inspect(engine)

    tables = inspector.get_table_names()

    schema = ""

    for table in tables:
        schema += f"{table}:\n"

        columns = inspector.get_columns(table)

        for column in columns:
            schema += f"- {column['name']} ({column['type']})\n"

        schema += "\n"

    return schema