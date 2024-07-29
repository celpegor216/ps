N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

result = [1] * N

for i in range(N - 1):
    for j in range(i + 1, N):
        if lst[i][0] > lst[j][0] and lst[i][1] > lst[j][1]:
            result[j] += 1
        elif lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            result[i] += 1

print(*result)