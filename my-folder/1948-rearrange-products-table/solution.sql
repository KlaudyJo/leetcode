# Write your MySQL query statement below


select product_id, 'store1' store, store1 price
FROM Products
where store1 IS NOT NULL
UNION
select product_id, 'store2' store, store2 price
FROM Products
where store2 IS NOT NULL
UNION
select product_id, 'store3' store, store3 price
FROM Products
where store3 IS NOT NULL;
