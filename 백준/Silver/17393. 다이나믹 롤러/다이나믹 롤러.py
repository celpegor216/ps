# 힌트: 이분탐색

N = int(input())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

result = [0] * N

for i in range(N - 1):
    start, end = i + 1, N - 1

    temp = 0

    while start <= end:
        middle = (start + end) // 2

        if lst1[i] < lst2[middle]:
            end = middle - 1
        else:
            temp = middle
            start = middle + 1
        
    if temp:
        result[i] = temp - i

print(*result)