T = int(input())
MAX = 200    # 팀 번호는 최대 200

for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    # 팀의 주자가 5명 이하인 팀을 가려내기 위해, 먼저 각 팀의 주자 수를 카운팅
    teams_cnt = [0] * (MAX + 1)

    for team in lst:
        teams_cnt[team] += 1

    # teams[i]: i번째 팀에 포함된 주자들의 점수 목록, 오름차순으로 정렬됨
    teams = [[] for _ in range(MAX + 1)]

    score = 0
    for n in range(N):
        team = lst[n]    # n번째로 들어온 주자의 팀 번호
        # 팀의 주자가 6명인 팀만 포함시켜서 점수 매기기
        if teams_cnt[team] == 6:
            score += 1
            teams[team].append(score)

    # 각 팀을 돌면서
    min_v = 21e8    # 최소 점수
    min_team = -1    # 최소 점수를 가진 팀 번호
    for m in range(1, MAX + 1):
        # 팀의 주자가 5명 이하라서 아무런 점수도 기록되지 않은 팀은 스킵
        if not teams[m]:
            continue

        # 팀 점수는 상위 네 명의 주자의 점수를 합하여 계산
        v = sum(teams[m][:4])

        # 동점의 경우에는 다섯 번째 주자가 가장 빨리 들어온 팀이 우승
        if min_v > v or (min_v == v and teams[min_team][-2] > teams[m][-2]):
            min_v = v
            min_team = m

    print(min_team)