-- Write your PostgreSQL query statement below
select customer_id
from Customers
where year = 2021
group by customer_id, year
having sum(revenue) > 1;
