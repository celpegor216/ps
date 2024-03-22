SELECT ID, FISH_NAME, LENGTH
FROM FISH_INFO, FISH_NAME_INFO
WHERE FISH_INFO.FISH_TYPE = FISH_NAME_INFO.FISH_TYPE
    AND (FISH_INFO.FISH_TYPE, LENGTH) IN (
        SELECT FISH_TYPE, MAX(LENGTH)
        FROM FISH_INFO AS A
        GROUP BY FISH_TYPE
    )
ORDER BY ID