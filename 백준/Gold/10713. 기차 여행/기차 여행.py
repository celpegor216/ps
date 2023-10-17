# 시간초과, 누적합인 것 같긴 했는데 방법이 떠오르지 않음

# 해답: https://velog.io/@7h13200/Python%EB%B0%B1%EC%A4%80-10713%EB%B2%88-%EA%B8%B0%EC%B0%A8-%EC%97%AC%ED%96%89
# 시작점에서 +1, 종료점에서 -1 => 누적합하면 시작점부터 종료점 이전까지 1씩 더하게 됨

N, M = map(int, input().split())

# 각 철도를 몇 번씩 이용하는지 횟수 계산
order = list(map(int, input().split()))
used = [0] * (N + 1)

for m in range(M - 1):
    a, b = order[m], order[m + 1]

    if a > b:
        a, b = b, a
    
    used[a] += 1
    used[b] -= 1

# 그냥 티켓 구입하는 게 더 싼지, IC 카드 사용하는 게 더 싼지 계산
costs = [list(map(int, input().split())) for _ in range(N - 1)]

result = 0
cnt = 0

for n in range(N - 1):
    cnt += used[n + 1]

    a, b, c = costs[n]

    result += min(a * cnt, b * cnt + c)

print(result)