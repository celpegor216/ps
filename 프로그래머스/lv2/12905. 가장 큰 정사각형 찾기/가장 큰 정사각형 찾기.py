# 해답: https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%A0%95%EC%82%AC%EA%B0%81%ED%98%95-%EC%B0%BE%EA%B8%B0-%EB%8F%99%EC%A0%81-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-dp

def solution(board):
    N = len(board)
    M = len(board[0])
    
    dp = [[0] * M for _ in range(N)]
    dp[0] = board[0][:]
    for i in range(N):
        dp[i][0] = board[i][0]
    
    for n in range(1, N):
        for m in range(1, M):
            if board[n][m]:
                dp[n][m] = min(dp[n - 1][m - 1], dp[n - 1][m], dp[n][m - 1]) + 1
    
    answer = 0
    
    for n in range(N):
        for m in range(M):
            if dp[n][m] > answer:
                answer = dp[n][m]

    return answer ** 2