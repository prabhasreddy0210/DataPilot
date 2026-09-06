from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy import text

from database.connection import engine
from app.services.sql_service import validate_sql
from app.services.llm_service import generate_sql, correct_sql


router = APIRouter()


class QueryRequest(BaseModel):
    question: str


@router.post("/query")
def execute_query(request: QueryRequest):

    question = request.question

    # Generate SQL using Gemini
    try:
        sql = generate_sql(question)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"AI SQL generation failed: {str(e)}"
        )

    max_attempts = 3

    for attempt in range(max_attempts):

        # Validate SQL
        is_valid, message = validate_sql(sql)

        if not is_valid:

            if attempt == max_attempts - 1:
                raise HTTPException(
                    status_code=400,
                    detail=f"SQL validation failed: {message}"
                )

            sql = correct_sql(
                question,
                sql,
                message
            )

            continue

        # Execute SQL
        try:
            with engine.connect() as connection:

                result = connection.execute(text(sql))

                rows = result.fetchall()
                columns = result.keys()

                data = []

                for row in rows:
                    data.append(dict(zip(columns, row)))

            return {
                "question": question,
                "sql": sql,
                "columns": list(columns),
                "rows": data
            }

        except Exception as e:

            error = str(e)

            if attempt == max_attempts - 1:
                raise HTTPException(
                    status_code=400,
                    detail=f"Query execution failed: {error}"
                )

            sql = correct_sql(
                question,
                sql,
                error
            )

    raise HTTPException(
        status_code=400,
        detail="Unable to generate a valid SQL query."
    )