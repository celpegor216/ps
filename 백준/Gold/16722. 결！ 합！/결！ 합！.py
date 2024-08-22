# ‘합’ 외치기
# ‘합’이라고 생각되는 서로 다른 그림 세 장의 번호를 외친다. 외친 번호의 그림 세 장이 ‘합’을 이루면서 이전에 외친 적이 없는 그림 조합이라면 +1점을, 아니라면 -1점을 획득한다.
# ‘결’ 외치기
# 아홉 장의 그림으로 조합 가능한 '합'들 중 외치지 않은 ‘합’이 더 이상 없다고 생각될 경우 ‘결’을 외친다. 실제로 외치지 않은 ‘합’ 이 없고 ‘결’을 통해 +3점을 얻은 적이 없다면 +3점을, 아니라면 -1점을 획득한다.


# 합을 이루는 모든 조합을 미리 찾아서 딕셔너리에 저장
N = 9
lst = [input().split() for _ in range(N)]
dic = dict()

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            flags = [[] for _ in range(3)]

            for n in range(3):
                for a, b in ((i, j), (i, k), (j, k)):
                    flags[n].append(1 if lst[a][n] == lst[b][n] else 0)

            for line in flags:
                if sum(line) not in (0, 3):
                    break
            else:
                dic[(i + 1, j + 1, k + 1)] = 0

has_g = 0
cnt = 0
result = 0

Q = int(input())
for _ in range(Q):
    cmd = input().split()

    # 합을 외칠 때마다 해당 딕셔너리의 값이 0이면 점수 + 1 & 합 카운트 + 1, 아니면 점수 - 1
    if cmd[0] == 'H':
        nums = tuple(sorted(map(int, cmd[1:])))
        if nums in dic and not dic[nums]:
            result += 1
            cnt += 1
            dic[nums] = 1
        else:
            result -= 1

    # 결을 외칠 때마다 합 카운트 == 딕셔너리 크기 & 이전에 결을 사용한 적이 없으면 + 3, 아니라면 - 1
    else:
        if not has_g and cnt == len(dic):
            result += 3
            has_g = 1
        else:
            result -= 1

print(result)