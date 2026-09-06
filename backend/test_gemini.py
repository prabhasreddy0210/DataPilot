from app.services.llm_service import generate_sql


question = "Show me all products that cost more than 20000"

sql = generate_sql(question)


print("\nGenerated SQL:")
print(sql)