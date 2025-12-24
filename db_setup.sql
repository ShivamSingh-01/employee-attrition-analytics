-- Create database
CREATE DATABASE IF NOT EXISTS employee_attrition_db;
USE employee_attrition_db;

-- Create employees table
CREATE TABLE IF NOT EXISTS employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    age INT,
    department VARCHAR(50),
    salary INT,
    years_at_company INT,
    job_role VARCHAR(50),
    attrition VARCHAR(5)
);

-- Insert sample data
INSERT INTO employees (age, department, salary, years_at_company, job_role, attrition) VALUES
(25, 'IT', 30000, 1, 'Developer', 'Yes'),
(30, 'HR', 40000, 3, 'HR Executive', 'No'),
(28, 'IT', 35000, 2, 'Developer', 'Yes'),
(45, 'Finance', 70000, 10, 'Manager', 'No'),
(35, 'Sales', 45000, 5, 'Sales Executive', 'Yes'),
(40, 'IT', 80000, 12, 'Tech Lead', 'No'),
(26, 'Sales', 32000, 1, 'Sales Executive', 'Yes'),
(50, 'HR', 90000, 15, 'HR Manager', 'No');

SELECT COUNT(*) FROM employees;

SELECT * FROM employees LIMIT 20;
