-- 코드를 입력하세요
SELECT a.flavor
FROM (select * from FIRST_HALF UNION
select * from JULY) as a
group by a.flavor
order by sum(a.total_order) desc
limit 3