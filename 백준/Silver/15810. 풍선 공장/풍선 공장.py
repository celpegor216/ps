# 해답: https://jinho-study.tistory.com/m/1028

N, M = map(int, input().split())
lst = list(map(int, input().split()))

start, end = 0, max(lst) * M    # 최소 시간, 최대 시간
result = 0

while start <= end:
    middle = (start + end) // 2

    if sum([middle // x for x in lst]) >= M:
        result = middle
        end = middle - 1
    else:
        start = middle + 1

print(result)