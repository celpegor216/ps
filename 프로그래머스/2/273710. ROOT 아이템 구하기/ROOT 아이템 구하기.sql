SELECT ITEM_INFO.ITEM_ID, ITEM_NAME
FROM ITEM_INFO, ITEM_TREE
WHERE ITEM_INFO.ITEM_ID = ITEM_TREE.ITEM_ID AND PARENT_ITEM_ID IS NULL
ORDER BY ITEM_INFO.ITEM_ID