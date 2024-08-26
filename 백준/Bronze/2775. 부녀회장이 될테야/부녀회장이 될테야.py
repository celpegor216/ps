T = int(input())

N = 14

# memo[a][b]: a층 b호에 살기 위해 데려와야 하는 사람의 수
# 아파트는 0층부터 최대 14층까지 있을 수 있음 -> _의 range를 N + 1까지
# 각 층은 1호부터 있지만, 계산을 편리하게 하기 위해 0호부터 있는 것으로 가정 -> [0] * (N + 1)
# 이때, 0호에는 0명이 사는 것으로 하면 계산에 차질이 생기지 않음
memo = [[0] * (N + 1) for _ in range(N + 1)]

# 0층
# j호에는 j명이 산다
for j in range(1, N + 1):
    memo[0][j] = j

# 1층부터 14층까지
for i in range(1, N + 1):
    for j in range(1, N + 1):
        # i층 j호에 살려면, i - 1층의 1호부터 j호까지 사람들의 수를 합한 만큼 사람이 필요
        # 이때, i층의 j - 1호에 i - 1층의 1호부터 j - 1호까지의 사람들 수가 기록되어 있으므로
        # i층의 j - 1호 + i - 1층의 j호 == i층 j호
        memo[i][j] = memo[i][j - 1] + memo[i - 1][j]

for _ in range(T):
    K = int(input())
    N = int(input())
    print(memo[K][N])