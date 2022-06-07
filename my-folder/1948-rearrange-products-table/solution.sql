/* Write your T-SQL query statement below */

SELECT product_id, store, price
FROM Products
UNPIVOT
(
price
for store in (store1, store2, store3))
as StorePivot;
