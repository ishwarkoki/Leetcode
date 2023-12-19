/* Write your T-SQL query statement below */ 

select max(salary) SecondHighestSalary  
from Employee 
where salary < (select max(salary) from Employee)

