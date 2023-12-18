/* Write your T-SQL query statement below */ 

with num_count as (
    select num, count(num) as number_count 
    from myNumbers
    group by num
) 

select max(num) as num 
from num_count 
where number_count = 1 