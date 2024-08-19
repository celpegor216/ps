def check(a, b):    # a국가와 b국가 간 경기
    global result

    if a == 5:
        result = 1
        return

    na = a
    nb = b + 1
    if nb == 6:
        na += 1
        nb = na + 1
    if teams[a][0] and teams[b][-1]:    # a국가가 이기는 경우
        teams[a][0] -= 1
        teams[b][-1] -= 1
        check(na, nb)
        if result: return
        teams[a][0] += 1
        teams[b][-1] += 1

    if teams[a][1] and teams[b][1]:    # 무승부인 경우
        teams[a][1] -= 1
        teams[b][1] -= 1
        check(na, nb)
        if result: return
        teams[a][1] += 1
        teams[b][1] += 1

    if teams[a][-1] and teams[b][0]:    # b국가가 이기는 경우
        teams[a][-1] -= 1
        teams[b][0] -= 1
        check(na, nb)
        if result: return
        teams[a][-1] += 1
        teams[b][0] += 1


TC = 4

for _ in range(TC):
    teams = list(map(int, input().split()))

    result = 0
    if sum(teams) == 30:
        teams = [teams[i:i + 3] for i in range(0, 18, 3)]
        check(0, 1)

    print(result, end=' ')