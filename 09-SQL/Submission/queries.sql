-----queries---

select e.emp_no, e.last_name, e.first_name, e.gender, s.salary
from employees as e
left join salaries as s
on e.emp_no = s.emp_no;


select * from employees;

select first_name, last_name, hire_date
from employees
where hire_date between '1986/1/1' and '1986/12/31';


select d.dept_no, d.dept_name, m.emp_no, e.last_name, e.first_name
from departments as d
left join dept_manager as m
on d.dept_no = m.dept_no
left join employees as e
on m.emp_no = e.emp_no;

select e.emp_no, e.last_name, e.first_name, d.dept_name
from dept_emp as de
left join departments as d
on de.dept_no = d.dept_no
left join employees as e
on de.emp_no = e.emp_no;

select e.first_name, e.last_name, e.gender
from employees as e
where e.first_name = 'Hercules' 
and e.last_name like 'B%';


SELECT dept_emp.emp_no, employees.last_name, employees.first_name, departments.dept_name
FROM dept_emp
JOIN employees
ON dept_emp.emp_no = employees.emp_no
JOIN departments
ON dept_emp.dept_no = departments.dept_no
WHERE departments.dept_name = 'Sales';

SELECT dept_emp.emp_no, employees.last_name, employees.first_name, departments.dept_name
FROM dept_emp
JOIN employees
ON dept_emp.emp_no = employees.emp_no
JOIN departments
ON dept_emp.dept_no = departments.dept_no
WHERE departments.dept_name = 'Sales' 
OR departments.dept_name = 'Development';


SELECT last_name,
COUNT(last_name) AS "frequency"
FROM employees
GROUP BY last_name
ORDER BY
COUNT(last_name) DESC;