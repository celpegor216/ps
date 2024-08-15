from collections import deque

N, M, K = map(int, input().split())
lst = [input() for _ in range(N)]

q = deque()
q.append((0, 0, 0, 1, 0))

used = [[[21e8] * (K + 1) for _ in range(M)] for _ in range(N)]
used[0][0][0] = 1

result = 21e8
while q:
    y, x, k, cnt, is_day = q.popleft()

    if used[y][x][k] < cnt or result < cnt:
        continue

    if y == N - 1 and x == M - 1:
        result = min(result, cnt)
        continue

    nxt_day = 0 if is_day else 1
    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M:
            if lst[ny][nx] == '1' and k < K:
                # 지금이 낮이어서 반나절 기다렸다 가는 경우
                if is_day and used[ny][nx][k + 1] > cnt + 2:
                    used[ny][nx][k + 1] = cnt + 2
                    q.append((ny, nx, k + 1, cnt + 2, is_day))
                # 지금이 밤이어서 다음에 바로 가는 경우
                elif nxt_day and used[ny][nx][k + 1] > cnt + 1:
                    used[ny][nx][k + 1] = cnt + 1
                    q.append((ny, nx, k + 1, cnt + 1, nxt_day))
            elif lst[ny][nx] == '0':
                if used[ny][nx][k] > cnt + 1:
                    used[ny][nx][k] = cnt + 1
                    q.append((ny, nx, k, cnt + 1, nxt_day))

print(result if result != 21e8 else -1)