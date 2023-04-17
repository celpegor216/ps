-- 코드를 입력하세요
SELECT I.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO I, REST_REVIEW R
WHERE I.REST_ID = R.REST_ID AND ADDRESS LIKE '서울%'
GROUP BY I.REST_ID
ORDER BY SCORE DESC, FAVORITES DESC;