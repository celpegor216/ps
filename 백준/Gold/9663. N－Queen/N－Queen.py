N = int(input())

col = [0] * N
lurd = [0] * N * 2    # 왼쪽 위 - 오른쪽 아래 대각선, 행 인덱스 - 열 인덱스 + N
ldru = [0] * N * 2    # 왼쪽 아래 - 오른쪽 위 대각선, 행 인덱스 + 열 인덱스

result = 0
def dfs(level):
    global result

    if level == N:
        result += 1
        return

    for i in range(N):    # 체스판의 level번째 행, i번째 열에 놓을 수 있는지 확인
        if not col[i] and not lurd[level - i + N] and not ldru[level + i]:
            col[i] = 1
            lurd[level - i + N] = 1
            ldru[level + i] = 1
            dfs(level + 1)
            col[i] = 0
            lurd[level - i + N] = 0
            ldru[level + i] = 0

dfs(0)

print(result)