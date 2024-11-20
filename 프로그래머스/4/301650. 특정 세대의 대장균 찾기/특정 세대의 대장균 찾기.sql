WITH RECURSIVE GenerationTree AS (
    -- 1세대 대장균을 초기 세대로 선택 (Anchor Query)
    SELECT 
        ID, 
        PARENT_ID, 
        1 AS Generation
    FROM 
        ECOLI_DATA
    WHERE 
        PARENT_ID IS NULL
    
    UNION ALL
    
    -- 자식 개체를 재귀적으로 탐색하며 세대 필드 반영 (Recursive Query)
    SELECT 
        e.ID, 
        e.PARENT_ID, 
        gt.Generation + 1 AS Generation
    FROM 
        ECOLI_DATA e
    INNER JOIN 
        GenerationTree gt
    ON 
        e.PARENT_ID = gt.ID
)
-- 3세대인 개체들의 ID를 선택하고 오름차순 정렬
SELECT ID
FROM GenerationTree
WHERE Generation = 3
ORDER BY ID;