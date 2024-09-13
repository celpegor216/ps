from collections import deque

# N*N, M개의 버섯 포자, K개의 연결된 칸에 자람
N, M, K = map(int, input().split())
# 자랄 수 있는 칸은 0, 버섯이 자랄 수 없는 칸은 1
lst = [list(map(int, input().split())) for _ in range(N)]

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

used = [[0] * N for _ in range(N)]

def check():
    result = 0

    for i in range(N):
        for j in range(N):
            if lst[i][j] or used[i][j]:
                continue

            q = deque()
            q.append((i, j))

            used[i][j] = 1

            cnt = 1

            while q:
                y, x = q.popleft()

                for dy, dx, in directions:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < N and not lst[ny][nx] and not used[ny][nx]:
                        cnt += 1
                        used[ny][nx] = 1
                        q.append((ny, nx))

            result += cnt // K
            if cnt % K:
                result += 1

            if result > M:
                return -1

    return result

result = check()

if result < 1:
    print('IMPOSSIBLE')
else:
    print('POSSIBLE')
    print(M - result)