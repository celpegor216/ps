# 이분 탐색인 것만 알겠음
# 해답: https://velog.io/@myway00/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-261%EB%B2%88-%EB%B0%B1%EC%A4%80-%EB%B2%88

N, T = map(int, input().split())
lst = []

min_total = 0
max_total = 0
start, end = 0, 0

for n in range(N):
    l, r = map(int, input().split())
    lst.append((l, r))
    min_total += l
    max_total += r
    start = max(start, l)
    end = max(end, r)

result = 10 ** 9 + 1

if min_total <= T and max_total >= T:
    while start <= end:
        middle = (start + end) // 2

        check = T
        cover = 0
        for item in lst:
            check -= item[0]
            
            if item[1] > middle:
                cover += middle - item[0]
            else:
                cover += item[1] - item[0]
        
        if cover >= check:
            result = min(result, middle)
            end = middle - 1
        else:
            start = middle + 1

if result == 10 ** 9 + 1:
    print(-1)
else:
    print(result)