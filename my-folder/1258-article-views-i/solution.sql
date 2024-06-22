-- Write your PostgreSQL query statement below

select author_id as id
from Views
where viewer_id = author_id
group by author_id
having count(view_date) > 0
order by author_id
