import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_mysql_password",
    database="employee_attrition_db"
)

df = pd.read_sql("SELECT * FROM employees", conn)

# Attrition by department
attrition_dept = df[df["attrition"] == "Yes"].groupby("department").count()["emp_id"]

plt.figure()
attrition_dept.plot(kind="bar")
plt.title("Attrition by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.show()

conn.close()
