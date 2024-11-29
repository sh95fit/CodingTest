SELECT E.ID AS ID, COUNT(D.PARENT_ID) AS CHILD_COUNT FROM ECOLI_DATA E
LEFT JOIN ECOLI_DATA D ON E.ID = D.PARENT_ID
GROUP BY E.ID
ORDER BY E.ID ASC