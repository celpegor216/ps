N = int(input())
lst = sorted(map(int, input().split()))

M = int(input())
targets = list(map(int, input().split()))

result = [0] * M

for m in range(M):
    start = 0
    end = N - 1

    while start <= end:
        middle = (start + end) // 2

        if lst[middle] == targets[m]:
            result[m] = 1
            break
        elif lst[middle] > targets[m]:
            end = middle - 1
        else:
            start = middle + 1

print(*result)