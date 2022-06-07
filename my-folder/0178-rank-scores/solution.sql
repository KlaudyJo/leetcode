# Write your MySQL query statement below

SELECT 
    s.Score,
    (
    SELECT COUNT(DISTINCT S2.Score)
    FROM Scores AS s2
    WHERE s2.Score >= s.Score    
    ) AS 'Rank'
FROM Scores AS s
ORDER BY s.Score DESC;
