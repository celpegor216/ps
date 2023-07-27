N, ATK = map(int, input().split())
# 몬스터: 1, 공격력, 생명력
# 포션: 2, 공격력, 생명력
lst = [list(map(int, input().split())) for _ in range(N)]

result = 1
HP = 1
for n in range(N):
    if lst[n][0] == 1:
        # 전투 진행 시 용사가 먼저 공격
        times = lst[n][2] // ATK
        if not lst[n][2] % ATK:
            times -= 1
        HP += lst[n][1] * times
        result = max(result, HP)
    else:
        ATK += lst[n][1]
        if HP > lst[n][2] + 1:
            HP -= lst[n][2]
        else:
            HP = 1

print(result)