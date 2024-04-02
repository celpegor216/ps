import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted([int(input()) for _ in range(N)])

result = lst[-1] - lst[0]

for i in range(N - 1):
    start, end = i, N - 1
    idx = end

    while start <= end:
        middle = (start + end) // 2

        diff = abs(lst[i] - lst[middle])

        if diff == M:
            result = diff
            break
        elif diff > M:
            result = min(result, diff)
            end = middle - 1
        else:
            start = middle + 1
    
    if result == M:
        break

print(result)