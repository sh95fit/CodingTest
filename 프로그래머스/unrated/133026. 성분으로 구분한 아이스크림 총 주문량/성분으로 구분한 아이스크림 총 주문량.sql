-- 코드를 입력하세요
SELECT I.INGREDIENT_TYPE, SUM(F.TOTAL_ORDER) AS TOTAL_ORDER FROM ICECREAM_INFO I
INNER JOIN FIRST_HALF F ON I.FLAVOR = F.FLAVOR
GROUP BY 1
ORDER BY 2