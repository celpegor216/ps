from collections import deque

N, M, R = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
used = [[0] * M for _ in range(N)]

result = 0
directions = {'E': (0, 1), 'S': (1, 0), 'W': (0, -1), 'N': (-1, 0)}

for _ in range(R):
    # 공격
    y, x, d = input().split()
    y = int(y) - 1
    x = int(x) - 1

    if not used[y][x]:
        used[y][x] = 1
        cnt = 1

        q = deque()
        q.append((y, x))

        while q:
            y, x = q.popleft()

            for i in range(1, lst[y][x]):
                ny, nx = y + directions[d][0] * i, x + directions[d][1] * i
                if 0 <= ny < N and 0 <= nx < M and not used[ny][nx]:
                    used[ny][nx] = 1
                    q.append((ny, nx))
                    cnt += 1

        result += cnt

    # 수비
    y, x = map(int, input().split())
    used[y - 1][x - 1] = 0

print(result)
for line in used:
    for item in line:
        print('F' if item else 'S', end=' ')
    print()