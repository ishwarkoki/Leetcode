# Write your MySQL query statement below 

with cte as (
  select *, count(pid) over(partition by tiv_2015) as tiv_2015_count, count(pid) over(partition by lat,lon) as location_count 
  from Insurance 
)

select round(sum(tiv_2016),2) as tiv_2016 
from cte 
where tiv_2015_count > 1 and location_count = 1 
