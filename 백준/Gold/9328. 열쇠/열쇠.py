# 메모리 초과
# 해답: https://ji-gwang.tistory.com/449


from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    lst = ['.' * (M + 2)] + ['.' + input() + '.' for _ in range(N)] + ['.' * (M + 2)]
    keys = input()

    q = deque()
    q.append((0, 0))
    used = [[0] * (M + 2) for _ in range(N + 2)]
    used[0][0] = 1

    results = set()

    while q:
        y, x = q.popleft()

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N + 2 and 0 <= nx < M + 2 and not used[ny][nx] and lst[ny][nx] != '*':
                if lst[ny][nx].isupper() and lst[ny][nx].lower() not in keys:
                    continue
                elif lst[ny][nx].islower() and lst[ny][nx] not in keys:
                    keys += lst[ny][nx]
                    used = [[0] * (M + 2) for _ in range(N + 2)]
                elif lst[ny][nx] == '$':
                    results.add((ny, nx))
            
                q.append((ny, nx))
                used[ny][nx] = 1

    print(len(results))