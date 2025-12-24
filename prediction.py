import mysql.connector
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_mysql_password",
    database="employee_attrition_db"
)

df = pd.read_sql("SELECT * FROM employees", conn)

# Encode categorical data
le = LabelEncoder()
df["department"] = le.fit_transform(df["department"])
df["job_role"] = le.fit_transform(df["job_role"])
df["attrition"] = df["attrition"].map({"Yes": 1, "No": 0})

X = df[["age", "salary", "years_at_company", "department", "job_role"]]
y = df["attrition"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

prediction = model.predict(X_test)

print("Predicted Attrition:", prediction.tolist())

conn.close()
