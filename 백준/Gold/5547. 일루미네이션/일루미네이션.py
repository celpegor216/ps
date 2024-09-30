M, N = map(int, input().split())
lst = [[0] * (M + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (M + 2)]

directions = (
    # i가 짝수일 때
    ((-1, -1), (-1, 0), (0, 1), (1, 0), (1, -1), (0, -1)),

    # i가 홀수일 때
    ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (0, -1)),
)


result = 0
used = [[0] * (M + 2) for _ in range(N + 2)]
used[0][0] = 1

q = [(0, 0)]

while q:
    nq = []

    for y, x in q:
        for dy, dx in directions[y % 2]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N + 2 and 0 <= nx < M + 2 and not used[ny][nx]:
                if lst[ny][nx]:
                    result += 1
                else:
                    used[ny][nx] = 1
                    nq.append((ny, nx))

    q = nq

print(result)