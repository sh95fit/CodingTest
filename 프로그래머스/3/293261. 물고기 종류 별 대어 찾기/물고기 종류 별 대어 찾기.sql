SELECT I.ID, N.FISH_NAME, I.LENGTH FROM FISH_INFO I
JOIN FISH_NAME_INFO N ON I.FISH_TYPE = N.FISH_TYPE
WHERE I.LENGTH = (
    SELECT MAX(I2.LENGTH)
    FROM FISH_INFO I2
    WHERE I2.FISH_TYPE = I.FISH_TYPE
)
ORDER BY 1