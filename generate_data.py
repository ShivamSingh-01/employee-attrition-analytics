import mysql.connector
import random

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_mysql_password",
    database="employee_attrition_db"
)

cursor = conn.cursor()

departments = ["IT", "HR", "Sales", "Finance"]
roles = {
    "IT": ["Developer", "Tester", "Tech Lead"],
    "HR": ["HR Executive", "HR Manager"],
    "Sales": ["Sales Executive", "Sales Manager"],
    "Finance": ["Accountant", "Finance Manager"]
}

def decide_attrition(age, salary, years, dept):
    score = 0
    if salary < 40000:
        score += 1
    if years <= 2:
        score += 1
    if age < 30:
        score += 1
    if dept in ["IT", "Sales"]:
        score += 1

    return "Yes" if score >= 2 else "No"

for _ in range(300):  # 🔥 300 EMPLOYEES
    age = random.randint(22, 55)
    years = random.randint(0, 20)
    salary = random.randint(25000, 120000)
    dept = random.choice(departments)
    role = random.choice(roles[dept])

    attrition = decide_attrition(age, salary, years, dept)

    cursor.execute(
        """
        INSERT INTO employees (age, department, salary, years_at_company, job_role, attrition)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (age, dept, salary, years, role, attrition)
    )

conn.commit()
conn.close()

print("✅ 300 realistic employee records inserted")
