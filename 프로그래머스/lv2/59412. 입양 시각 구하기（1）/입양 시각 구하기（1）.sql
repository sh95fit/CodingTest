-- 코드를 입력하세요
SELECT date_format(DATETIME, '%H') AS HOUR, COUNT(ANIMAL_ID) AS COUNT FROM ANIMAL_OUTS
WHERE date_format(DATETIME, '%H') BETWEEN '09' AND '20'
GROUP BY HOUR
ORDER BY HOUR