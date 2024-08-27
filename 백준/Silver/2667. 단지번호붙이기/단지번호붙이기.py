from collections import deque

N = int(input())
lst = [input() for _ in range(N)]

used = [[0] * N for _ in range(N)]

result = []
for i in range(N):
    for j in range(N):
        if lst[i][j] == '0' or used[i][j]:
            continue

        q = deque()
        q.append((i, j))
        used[i][j] = 1
        cnt = 1

        while q:
            y, x = q.popleft()

            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N and lst[ny][nx] == '1' and not used[ny][nx]:
                    q.append((ny, nx))
                    used[ny][nx] = 1
                    cnt += 1

        result.append(cnt)

print(len(result))
for item in sorted(result):
    print(item)