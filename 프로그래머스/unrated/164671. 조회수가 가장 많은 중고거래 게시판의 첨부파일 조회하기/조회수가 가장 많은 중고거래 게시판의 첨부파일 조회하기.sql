-- 코드를 입력하세요
SELECT CONCAT_WS('/', "/home/grep/src", B.BOARD_ID, CONCAT(F.FILE_ID,F.FILE_NAME,FILE_EXT)) AS FILE_PATH 
FROM USED_GOODS_BOARD B
JOIN USED_GOODS_FILE F ON B.BOARD_ID = F.BOARD_ID
WHERE B.VIEWS = (SELECT MAX(B.VIEWS) FROM USED_GOODS_BOARD B)
ORDER BY F.FILE_ID DESC