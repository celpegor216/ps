N = int(input())
M = int(input())

# lst[n]: (n + 1)번 방의 오른쪽 벽
lst = [1] * (N - 1)

for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    for i in range(x, y):
        lst[i] = 0

print(sum(lst) + 1)