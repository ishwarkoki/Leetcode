# Write your MySQL query statement below  

select customer_id 
from Customer 
group by customer_id 
having count(distinct product_key) = (select count(product_key) from Product) ; 

# select customer_id from (
#   select customer_id, count(distinct product_key) as product_count 
#   from Customer 
#   group by customer_id
# ) c  where product_count = (select count(product_key) from Product) ; 
