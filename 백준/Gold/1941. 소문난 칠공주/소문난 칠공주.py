N = 5
lst = [input() for _ in range(N)]

result = 0
used = [[0] * N for _ in range(N)]
used_combinations = set()

def dfs(level, now, cnt_s, cnt_y):
    global result

    tup = tuple(sorted(now))

    if tup in used_combinations:    # 이미 선택했던 조합인 경우
        return

    used_combinations.add(tup)

    if cnt_y > 3:    # 임도연파가 우위를 점한 경우
        return

    if level == 7:
        result += 1
        return

    for num in now:
        y = num // N
        x = num % N
        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not used[ny][nx]:
                used[ny][nx] = 1
                if lst[ny][nx] == 'S':
                    dfs(level + 1, now + [ny * N + nx], cnt_s + 1, cnt_y)
                else:
                    dfs(level + 1, now + [ny * N + nx], cnt_s, cnt_y + 1)
                used[ny][nx] = 0

for i in range(N):
    for j in range(N):
        used[i][j] = 1
        if lst[i][j] == 'S':
            dfs(1, [i * N + j], 1, 0)
        else:
            dfs(1, [i * N + j], 0, 1)
        used[i][j] = 0

print(result)