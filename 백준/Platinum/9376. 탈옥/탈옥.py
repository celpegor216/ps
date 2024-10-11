# 반례 참고
# 0-1 bfs는 처음 풀어봄,,,
# 해답: https://paris-in-the-rain.tistory.com/123


from collections import deque


TC = int(input())


directions = ((0, 1), (1, 0), (0, -1), (-1, 0))


def bfs(sy, sx):
    # used[i][j]: sy, sx부터 i, j까지 가기 위해 열어야 하는 문의 개수
    used = [[-1] * (M + 2) for _ in range(N + 2)]

    q = deque()
    q.append((sy, sx))
    used[sy][sx] = 0

    while q:
        y, x = q.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < N + 2 and 0 <= nx < M + 2) or used[ny][nx] != -1 or lst[ny][nx] == '*':
                continue

            # 문을 열어야 하는 경우
            if lst[ny][nx] == '#':
                used[ny][nx] = used[y][x] + 1
                q.append((ny, nx))
            # 문을 열지 않아도 되는 경우
            else:
                used[ny][nx] = used[y][x]
                # 가장 앞에 삽입
                q.appendleft((ny, nx))

    return used


for _ in range(TC):
    N, M = map(int, input().split())
    lst = ['.' * (M + 2)] + ['.' + input() + '.' for _ in range(N)] + ['.' * (M + 2)]

    people = []
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if lst[i][j] == '$':
                people.append((i, j))

    distances_from_first_person = bfs(*people[0])
    distances_from_second_person = bfs(*people[1])
    distances_from_outside = bfs(0, 0)

    result = N * M
    for i in range(N + 2):
        for j in range(N + 2):
            if lst[i][j] == '*':
                continue

            # 첫 번째 사람도, 두 번째 사람도, 그리고 밖에서 들어온 사람도
            # 모두 방문할 수 있는 지점이라면 그 지점을 통해 밖으로 나갈 수 있음
            if distances_from_first_person[i][j] != -1 and distances_from_second_person[i][j] != -1 and distances_from_outside[i][j] != -1:
                total = distances_from_first_person[i][j] + distances_from_second_person[i][j] + distances_from_outside[i][j]

                # 벽이라면 한 명만 열면 되기 때문에 나머지 두 명이 열면서 더한 횟수를 다시 빼줌
                if lst[i][j] == '#':
                    total -= 2

                result = min(result, total)

    print(result)