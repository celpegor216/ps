from collections import deque


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

used = [[0] * M for _ in range(N)]

# i번째 그룹에 속한 칸의 수
group_cnt = [0]

group_idx = 1
for i in range(N):
    for j in range(M):
        if not lst[i][j] or used[i][j]:
            continue

        q = deque()
        q.append((i, j))
        used[i][j] = group_idx

        group_cnt.append(1)

        while q:
            y, x = q.popleft()

            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] and not used[ny][nx]:
                    group_cnt[-1] += 1
                    q.append((ny, nx))
                    used[ny][nx] = group_idx
        
        group_idx += 1


result = 0
for i in range(N):
    for j in range(M):
        if lst[i][j]:
            continue

        near_groups = set()
        for dy, dx in directions:
            ny, nx = i + dy, j + dx
            if 0 <= ny < N and 0 <= nx < M and used[ny][nx]:
                near_groups.add(used[ny][nx])
        
        total = 1
        for group in near_groups:
            total += group_cnt[group]
        
        result = max(result, total)

print(result)