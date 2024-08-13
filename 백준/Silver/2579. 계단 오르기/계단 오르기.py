N = int(input())
lst = [int(input()) for _ in range(N)]

if N <= 2:
    print(sum(lst))
else:
    # dp[0][n]: n과 n - 1칸을 골랐을 때의 최댓값
    # dp[1][n]: n과 n - 2칸을 골랐을 때의 최댓값
    dp = [[0] * N for _ in range(2)]

    dp[0][0] = lst[0]
    dp[1][0] = lst[0]
    dp[0][1] = sum(lst[:2])
    dp[1][1] = lst[1]

    for n in range(2, N):
        # n과 n - 1칸을 골랐을 경우, n - 2칸은 고를 수 없으므로 dp[1][n - 1]만 가능
        dp[0][n] = dp[1][n - 1] + lst[n]
        # n과 n - 2칸을 골랐을 경우, n - 3칸을 고르든 n - 4칸을 고르든 상관 없음
        # 따라서 dp[0][n - 2]와 dp[1][n - 2] 둘 중 더 큰 값을 취해야 함
        dp[1][n] = max(dp[0][n - 2], dp[1][n - 2]) + lst[n]

    print(max(dp[0][-1], dp[1][-1]))