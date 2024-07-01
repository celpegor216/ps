import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dots = sorted(map(int, input().split()))

for _ in range(M):
    s, e = map(int, input().split())

    left, right = 0, N - 1
    start = N

    while left <= right:
        middle = (left + right) // 2

        if dots[middle] >= s:
            start = min(start, middle)
            right = middle - 1
        else:
            left = middle + 1

    left, right = 0, N - 1
    end = -1

    while left <= right:
        middle = (left + right) // 2

        if dots[middle] <= e:
            end = max(end, middle)
            left = middle + 1
        else:
            right = middle - 1
    
    if end >= start:
        print(end - start + 1)
    else:
        print(0)