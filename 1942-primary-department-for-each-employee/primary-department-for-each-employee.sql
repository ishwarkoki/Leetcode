# Write your MySQL query statement below 

with emp_details as (
  select *, count(employee_id) over(partition by employee_id) as department_count 
  from Employee
) 

select employee_id, department_id from emp_details 
where department_count = 1 or primary_flag = 'Y' ; 

