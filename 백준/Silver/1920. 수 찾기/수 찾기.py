N = int(input())
lst = sorted(map(int, input().split()))
M = int(input())
queries = list(map(int, input().split()))

for m in range(M):
    start = 0
    end = N - 1
    result = 0

    while start <= end:
        middle = (start + end) // 2

        if lst[middle] == queries[m]:
            result = 1
            break
        elif lst[middle] > queries[m]:
            end = middle - 1
        else:
            start = middle + 1

    print(result)