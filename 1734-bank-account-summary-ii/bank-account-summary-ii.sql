# Write your MySQL query statement below

select u.name name , sum(t.amount) balance
from Transactions t LEFT join users u on t.account = u.account 
group by u.name 
having sum(t.amount) > 10000 