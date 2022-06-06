# Write your MySQL query statement below
select t.Id 
from Weather t, Weather as y
where datediff(t.recordDate, y.recordDate)= 1
and t.temperature > y.temperature;
