# Write your MySQL query statement below 
With non_red_sales as (
    select s.name 
    from salesPerson s left join Orders o on s.sales_id = o.sales_id left join Company c on o.com_id = c.com_id 
    where c.name = 'RED'
)

select name 
from salesPerson 
where name not in (select name from non_red_sales)

