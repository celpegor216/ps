TC = int(input())

def dfs(level, order):
    if level == M:
        combinations.append(order)
        return

    for i in range(M):
        if i in order:
            continue

        dfs(level + 1, order + [i])

# M개 순열
combinations_by_level = [[]]
for M in range(1, 6):
    combinations = []
    dfs(0, [])
    combinations_by_level.append(combinations)

for tc in range(1, TC + 1):
    # N*N, 꿀을 채취할 수 있는 벌통의 수 M, 채취할 수 있는 꿀의 최대 양 C
    N, M, C = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    # possibles[i]: i번째 위치에서 M개를 가로로 연속되도록 선택했을 때,
    #               그 총합이 C 이하인 경우 가치
    possibles = dict()

    for i in range(N):
        for j in range(N - M + 1):
            key = i * N + j

            # 각각의 일꾼은 가로로 연속되도록 M개의 벌통을 선택하고,
            # 선택한 벌통에서 꿀을 채취할 수 있다.
            # 하나의 벌통에서 채취한 꿀은 하나의 용기에 담아야 한다.
            # 이때 하나의 용기에 있는 꿀의 양이 많을수록 상품가치가 높아,
            # 각 용기에 있는 꿀의 양의 제곱만큼의 수익이 생긴다.

            # M개의 벌통에서 M개 모두 사용하지 않고 일부만 사용할 수도 있음
            max_value = 0
            for combination in combinations_by_level[M]:
                total = 0
                value = 0
                for m in combination:
                    if total + lst[i][j + m] > C:
                        break
                    total += lst[i][j + m]
                    value += lst[i][j + m] ** 2
                max_value = max(max_value, value)

            possibles[key] = max_value

    # 두 일꾼이 꿀을 채취하여 얻을 수 있는 수익의 합이 최대가 되는 경우를 찾고,
    # 그 때의 최대 수익을 출력
    # 단, 두 명의 일꾼이 선택한 벌통은 서로 겹치면 안 된다.
    result = 0
    keys = [key for key in possibles.keys()]
    length = len(keys)

    for i in range(length - 1):
        for j in range(i + 1, length):
            key1, key2 = keys[i], keys[j]
            # print(key1, key2, possibles[key1], possibles[key2])

            if abs(key1 - key2) < M:
                continue

            result = max(result, possibles[key1] + possibles[key2])

    print(f'#{tc} {result}')
