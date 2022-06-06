# Write your MySQL query statement below
select b.firstName, b.lastName, c.city, c.state
from Person b
left join address c 
on b.personId = c.personId;
