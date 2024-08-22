N = int(input())    # 이닝 수
lst = [list(map(int, input().split())) for _ in range(N)]

M = 9
# 1번 선수를 4번 타자로 미리 결정했다

result = 0
used = [0] * M
def dfs(level, order):
    global result

    if level == M:
        bases = [-1] * M    # i번째 타석에 위치한 선수의 인덱스
        for i in range(M):
            bases[order[i]] = i

        total = 0    # 이 배치대로 수행했을 때 얻을 수 있는 최대 점수
        now = 0    # 현재 나와있는 선수의 인덱스
        for n in range(N):    # 이닝 시작
            b1 = b2 = b3 = 0    # 현재 베이스 상태, 비어있으면 0
            out = 0    # 현재 이닝의 아웃 카운트
            while out < 3:
                if lst[n][bases[now]] == 0:
                    out += 1
                elif lst[n][bases[now]] == 1:
                    total += b3
                    b1, b2, b3 = 1, b1, b2
                elif lst[n][bases[now]] == 2:
                    total += b3 + b2
                    b1, b2, b3 = 0, 1, b1
                elif lst[n][bases[now]] == 3:
                    total += b3 + b2 + b1
                    b1, b2, b3 = 0, 0, 1
                else:
                    total += b3 + b2 + b1 + 1
                    b1 = b2 = b3 = 0
                now = (now + 1) % 9

        result = max(result, total)
        return

    # level번째 선수를 i번째 타석에 배치
    for i in range(M):
        if not used[i]:
            used[i] = 1
            dfs(level + 1, order + [i])
            used[i] = 0

used[3] = 1
dfs(1, [3])

print(result)