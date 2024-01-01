# 분할 정복, dp 같은데 풀리지 않음
# 해답: https://supersfel.tistory.com/210

T = int(input())

for t in range(T):
    K = int(input())
    lst = [0] + list(map(int, input().split()))
    sums = [0] * (K + 1)

    for i in range(1, K + 1):
        sums[i] = sums[i - 1] + lst[i]
    
    dp = [[0] * (K + 1) for _ in range(K + 1)]

    for i in range(2, K + 1):    # i개의 합을 구함
        for j in range(1, K + 2 - i):    # j부터 시작해서 i개
            dp[j][j + i - 1] = min([dp[j][j + k] + dp[j + k + 1][j + i - 1] for k in range(i - 1)]) + sums[j + i - 1] - sums[j - 1]
    
    print(dp[1][K])