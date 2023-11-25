# Write your MySQL query statement below 

with cte as (

  select max(turn) as turn_val 
  from (select person_id, person_name, turn, weight, sum(weight) over( order by turn ) total_weight 
        from Queue ) t 
  where total_weight <= 1000 
  
) 

select person_name 
from Queue 
where turn in (select turn_val from cte)