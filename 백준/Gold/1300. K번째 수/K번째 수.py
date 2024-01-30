# 해답: https://velog.io/@uoayop/BOJ-1300-K%EB%B2%88%EC%A7%B8-%EC%88%98Python

N = int(input())
K = int(input())

start, end = 0, K
result = 0

while start <= end:
    middle = (start + end) // 2

    # 크기가 N인 배열에서 middle보다 작은 곱 개수 찾기
    cnt = 0

    for i in range(1, N + 1):
        cnt += min(middle // i, N)

    if cnt >= K:
        result = middle
        end = middle - 1
    else:
        start = middle + 1

print(result)