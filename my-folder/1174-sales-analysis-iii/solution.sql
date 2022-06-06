# Write your MySQL query statement below

select product_id,product_name
from Product
where product_id not in (
    select product_id
    from Sales
    where sale_date not between '2019-01-01' and '2019-03-31'
);
