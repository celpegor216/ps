N = int(input())
lst = sorted(map(int, input().split()))

result = 0

for n in range(1, N):
    start = 0
    end = n - 1

    idx = n

    while start <= end:
        middle = (start + end) // 2

        if lst[middle] >= lst[n] * 0.9:
            idx = min(idx, middle)
            end = middle - 1
        else:
            start = middle + 1
    
    result += n - idx

print(result)