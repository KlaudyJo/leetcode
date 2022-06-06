# Write your MySQL query statement below
Update salary
set sex =  Case 
when sex = 'f' then 'm'
else 'f'
end;
