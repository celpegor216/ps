from collections import deque

N = 8
lst = [input() for _ in range(N)]

# walls[j]: j열에 있는 모든 벽의 행 위치, 오름차순으로 추가함
#           -> 미로를 움직일 때 해당 열에 벽이 있다면,
#              행이 가장 큰 마지막 위치를 남길 것인지만 판단하면 됨
walls = [[] for _ in range(N)]
for j in range(N):
    for i in range(N):
        if lst[i][j] == '#':
            walls[j].append(i)

q = deque()
q.append((N - 1, 0))

result = 0

directions = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 0))

# 최대 N번 미로가 움직이는데 그때까지 살아있을 수 있다면 됨
for n in range(N):
    # 캐릭터가 움직일 때 중복 위치 체크를 위함
    used = [[0] * N for _ in range(N)]

    # 캐릭터 움직이기
    for _ in range(len(q)):
        y, x = q.popleft()

        # 이전에 미로가 움직여서 현재 위치에 있는 경우
        if y - n in walls[x]:
            continue

        for dy, dx in directions:
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < N and ny - n not in walls[nx] and not used[ny][nx]:
                used[ny][nx] = 1
                q.append((ny, nx))

    # 미로 움직이기
    flag = 0

    for j in range(N):
        if walls[j] and walls[j][-1] + n == N - 1:
            walls[j].pop()

        if walls[j]:
            flag = 1

    if not q:  # 이동할 수 있는 위치가 없는 경우
        print(0)
        break
    elif not flag:  # 움직일 미로가 없는 경우
        print(1)
        break
