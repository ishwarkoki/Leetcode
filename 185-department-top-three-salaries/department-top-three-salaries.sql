# Write your MySQL query statement below
# Write your MySQL query statement below 
-- Table - employee, department 
-- top 3 salary ? 

select Department, Employee, Salary from (select d.name as Department, e.name as Employee, e.salary as Salary,
dense_rank() over(partition by d.name order by salary desc) as ranking
from employee e join department d on 
e.departmentId = d.id) as temptable where ranking<4 ;  


