N = int(input())
lst = [input() for _ in range(5)]

nums = ['###...#.###.###.#.#.###.###.###.###.###',
        '#.#...#...#...#.#.#.#...#.....#.#.#.#.#',
        '#.#...#.###.###.###.###.###...#.###.###',
        '#.#...#.#.....#...#...#.#.#...#.#.#...#',
        '###...#.###.###...#.###.###...#.###.###']

possibles = [[] for _ in range(N)]

for n in range(N):
    nx = 4 * n
    for num in range(10):
        flag = 0
        mx = 4 * num

        for i in range(5):
            if flag:
                break

            for j in range(3):
                if lst[i][nx + j] == '#' and nums[i][mx + j] == '.':
                    flag = 1
                    break

        if not flag:
            possibles[n].append(num)

flag = 0

for possible in possibles:
    if not possible:
        flag = 1
        break

if flag:
    print(-1)
else:
    result_total = 0
    result_cnt = 1

    for n in range(N):
        result_cnt *= len(possibles[n])

    for n in range(N):
        result_total += sum(possibles[n]) * 10 ** (N - 1 - n) * (result_cnt // len(possibles[n]))

    print(round(result_total / result_cnt, 6))