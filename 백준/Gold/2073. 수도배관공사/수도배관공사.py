# 총 길이 D, 매입한 파이프 개수 P
D, P = map(int, input().split())
# 길이 l, 용량 c
lst = [list(map(int, input().split())) for _ in range(P)]

# 수도관의 용량은 그것을 이루는 파이프들의 용량 중 최솟값
# 수도관의 길이는 파이프들 길이의 총합
# 가능한 최대 수도관 용량
# 길이와 용량은 최대 2 ** 23

# dp 같다
dp = [[0] * (D + 1) for _ in range(P)]
lst.sort(key=lambda x: (-x[1]))

for p in range(P):
    for d in range(1, D + 1):
        if lst[p][0] > d:
            dp[p][d] = dp[p - 1][d]
        elif lst[p][0] == d:
            dp[p][d] = max(dp[p - 1][d], lst[p][1])
        else:
            dp[p][d] = max(dp[p - 1][d], min(dp[p - 1][d - lst[p][0]], lst[p][1]))

print(dp[-1][-1])