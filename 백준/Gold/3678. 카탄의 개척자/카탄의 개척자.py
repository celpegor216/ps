directions = ((-1, 1), (-2, 0), (-1, -1), (1, -1), (2, 0), (1, 1))


y = x = 125
used = [[0] * 250 for _ in range(250)]
results = [0] * 10001
cnts = [0] * 6


idx = 1
d = 0
cnt = 0
max_cnt = 1
while idx <= 10000:
    used[y][x] = idx

    # results에 숫자 넣기
    impossibles = set()    # 인접한 타일에 들어있는 자원
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if results[used[ny][nx]]:
            impossibles.add(results[used[ny][nx]])
    selected = (21e8, 21e8)
    for i in range(1, 6):
        if i in impossibles:
            continue
        selected = min(selected, (cnts[i], i))
    results[idx] = selected[1]
    cnts[selected[1]] += 1

    idx += 1

    if d == 1 and cnt == max_cnt - 1:
        d += 1
        cnt = 0

    dy, dx = directions[d]
    y += dy
    x += dx

    cnt += 1
    if cnt == max_cnt:
        d += 1
        cnt = 0
        if d == 6:
            d = 0
            max_cnt += 1

TC = int(input())
for _ in range(TC):
    print(results[int(input())])