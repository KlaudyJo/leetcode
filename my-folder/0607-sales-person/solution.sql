# Write your MySQL query statement below
select name
from SalesPerson 
where sales_id not in (SELECT DISTINCT sales_id
                      from Orders
                      where com_id = (
                      select com_id from company where name = 'RED'));
