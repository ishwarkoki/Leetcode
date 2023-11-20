# Write your MySQL query statement below 

with customer_cte as (
  select visited_on, sum(amount) amount
  from customer
  group by visited_on 
) 

select visited_on, sum(amount) over(order by visited_on rows between 6 preceding and current row ) amount, round (avg(amount) over(order by visited_on rows between 6 preceding and current row), 2) average_amount
from customer_cte 
limit 18446744073709551615
offset 6 

 
