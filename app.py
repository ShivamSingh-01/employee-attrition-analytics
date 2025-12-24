import mysql.connector
import pandas as pd

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_mysql_password",
    database="employee_attrition_db"
)

query = "SELECT * FROM employees"
df = pd.read_sql(query, conn)

print("Employee Data:")
print(df)

conn.close()
