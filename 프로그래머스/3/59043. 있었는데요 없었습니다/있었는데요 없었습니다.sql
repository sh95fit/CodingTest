-- 코드를 입력하세요
SELECT I.ANIMAL_ID, I.NAME FROM ANIMAL_INS I
JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
AND O.DATETIME < I.DATETIME
ORDER BY I.DATETIME