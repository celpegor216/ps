# 해답: https://velog.io/@sugenius77/%EB%B0%B1%EC%A4%80Python-16967%EB%B2%88-%EB%B0%B0%EC%97%B4-%EB%B3%B5%EC%9B%90%ED%95%98%EA%B8%B0

H, W, X, Y = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H + X)]
result = [board[h][:W] for h in range(H)]

for i in range(X, H):
    for j in range(Y, W):
        result[i][j] = board[i][j] - result[i - X][j - Y]

for line in result:
    print(*line)