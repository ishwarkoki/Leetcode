/* Write your T-SQL query statement below */

-- with course_cte as (
--     select class, count(class) number_of_students
--     from Courses 
--     group by class 
-- )

select class
from Courses 
group by class 
having count(class) >= 5 