WITH EmployeeScores AS (
    SELECT EMP_NO, SUM(SCORE) AS SCORE
    FROM HR_GRADE
    WHERE YEAR = 2022
    GROUP BY EMP_NO
)
SELECT 
    eS.SCORE, 
    e.EMP_NO, 
    e.EMP_NAME, 
    e.POSITION, 
    e.EMAIL
FROM EmployeeScores eS
JOIN HR_EMPLOYEES e ON eS.EMP_NO = e.EMP_NO
WHERE eS.SCORE = (SELECT MAX(SCORE) FROM EmployeeScores);