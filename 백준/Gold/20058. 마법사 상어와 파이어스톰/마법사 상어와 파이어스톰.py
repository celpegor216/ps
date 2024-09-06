from collections import deque


# 2 ^ N × 2 ^ N인 격자
N, Q = map(int, input().split())
N = 2 ** N
# A[r][c]는 (r, c)에 있는 얼음의 양을 의미한다. A[r][c]가 0인 경우 얼음이 없는 것
lst = [list(map(int, input().split())) for _ in range(N)]
cmds = list(map(int, input().split()))
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

# 파이어스톰을 총 Q번 시전
for q in range(Q):
    L = 2 ** cmds[q]

    # 파이어스톰은 먼저 격자를 2 ^ L × 2 ^ L 크기의 부분 격자로 나눈다
    # 모든 부분 격자를 시계 방향으로 90도 회전
    for i in range(0, N, L):
        for j in range(0, N, L):
            tmp = [lst[k][j:j + L] for k in range(i, i + L)]
            tmp = list(map(list, zip(*tmp[::-1])))
            for k in range(L):
                lst[i + k][j:j + L] = tmp[k]

    # 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다
    checks = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not lst[i][j]:
                continue

            cnt = 0
            for dy, dx in directions:
                ny, nx = i + dy, j + dx
                if 0 <= ny < N and 0 <= nx < N and lst[ny][nx]:
                    cnt += 1
            if cnt < 3:
                checks[i][j] = 1

    for i in range(N):
        for j in range(N):
            if not lst[i][j]:
                continue

            lst[i][j] -= checks[i][j]

# 모든 파이어스톰을 시전한 후, 다음 2가지를 구해보자.
# 남아있는 얼음 A[r][c]의 합
print(sum([sum(line) for line in lst]))

# 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
maxv = 0
used = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if used[i][j] or not lst[i][j]:
            continue

        used[i][j] = 1
        q = deque()
        q.append((i, j))
        cnt = 1

        while q:
            y, x = q.popleft()

            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N and not used[ny][nx] and lst[ny][nx]:
                    used[ny][nx] = 1
                    q.append((ny, nx))
                    cnt += 1

        maxv = max(maxv, cnt)

print(maxv)