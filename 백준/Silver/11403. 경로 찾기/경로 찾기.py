from collections import deque

N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]
result = [[0] * N for _ in range(N)]

def bfs(start):
    q = deque()
    used = [0] * N

    q.append(start)

    while q:
        now = q.popleft()

        for i in range(N):
            if not used[i] and lst[now][i]:
                result[start][i] = 1
                used[i] = 1
                q.append(i)

for n in range(N):
    bfs(n)

for line in result:
    print(*line)