SELECT COUNT(*) AS FISH_COUNT, FISH_NAME
FROM FISH_INFO, FISH_NAME_INFO
WHERE FISH_INFO.FISH_TYPE = FISH_NAME_INFO.FISH_TYPE
GROUP BY FISH_NAME
ORDER BY FISH_COUNT DESC