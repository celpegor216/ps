# 우선순위 큐를 써서 가장 큰 구간부터 쪼개야하는 건 알겠는데
# 큰 구간을 어떻게 쪼개야하는지 모르겠음
# 해답: https://2hs-rti.tistory.com/entry/%EB%B0%B1%EC%A4%80-1477%EB%B2%88-%ED%9C%B4%EA%B2%8C%EC%86%8C-%EC%84%B8%EC%9A%B0%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

# 우선순위 큐가 아닌 이분탐색이었음,,,

N, M, L = map(int, input().split())
lst = [0] + sorted(map(int, input().split())) + [L]

start, end = 1, L - 1
result = end

while start <= end:
    middle = (start + end) // 2

    cnt = 0
    for n in range(1, N + 2):
        dist = lst[n] - lst[n - 1]
        if dist > middle:
            cnt += (dist - 1) // middle
    
    if cnt > M:
        start = middle + 1
    else:
        result = min(result, middle)
        end = middle - 1

print(result)