# Write your MySQL query statement below 
with cte as (
  select id, student, lead(student, 1) over(order by id) as next_val, lag(student, 1) over(order by id) as prev_val
  from seat
) 

select id, if(id%2 = 0,prev_val,coalesce(next_val, student)) as student 
from cte  
 

