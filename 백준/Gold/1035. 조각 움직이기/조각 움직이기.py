N = 5
lst = [input() for _ in range(N)]

cnt = 0
useds = []

for i in range(N):
    for j in range(N):
        if lst[i][j] == '.':
            continue

        used = [[0] * N for _ in range(N)]
        for y in range(N):
            for x in range(N):
                used[y][x] = abs(i - y) + abs(j - x)

        useds.append(used)
        cnt += 1


order = [-1] * cnt
def make_order(level):
    if level == cnt:
        orders.append(order[:])
        return

    for i in range(cnt):
        if i not in order:
            order[level] = i
            make_order(level + 1)
            order[level] = -1


directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
combination = []
def make_combinations(level):
    tup = tuple(sorted(combination))

    if tup in combinations:
        return
    combinations.add(tup)

    if level == cnt:
        return

    for y, x in combination:
        for dy, dx in directions:
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < N and (ny, nx) not in combination:
                combination.append((ny, nx))
                make_combinations(level + 1)
                combination.pop()

if cnt == 1:
    print(0)
else:
    result = 21e8
    orders = []
    make_order(0)

    combinations = set()
    for i in range(N):
        for j in range(N):
            combination.append((i, j))
            make_combinations(0)
            combination.pop()

    combinations = [combination for combination in combinations if len(combination) == cnt]

    for combination in combinations:
        for order in orders:
            total = 0
            for i in range(cnt):
                total += useds[order[i]][combination[i][0]][combination[i][1]]
            result = min(result, total)

    print(result)