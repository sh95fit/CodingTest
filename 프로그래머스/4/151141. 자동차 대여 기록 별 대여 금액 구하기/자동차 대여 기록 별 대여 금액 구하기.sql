SELECT H.HISTORY_ID, ROUND(C.DAILY_FEE*(100-IFNULL(P.DISCOUNT_RATE, 0))/100*(DATEDIFF(H.END_DATE,H.START_DATE)+1), 0) AS FEE FROM CAR_RENTAL_COMPANY_CAR C
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H ON C.CAR_ID = H.CAR_ID AND C.CAR_TYPE = '트럭'
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
ON C.CAR_TYPE = P.CAR_TYPE AND
DATEDIFF(H.END_DATE,H.START_DATE)+1 >= CAST(P.DURATION_TYPE AS UNSIGNED)
GROUP BY H.HISTORY_ID
ORDER BY FEE DESC, H.HISTORY_ID DESC