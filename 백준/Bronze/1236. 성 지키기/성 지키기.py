N, M = map(int, input().split())
lst = [input() for _ in range(N)]

# row[i]: i번째 행에 경비원이 있으면 1, 없으면 0
row = [0] * N
# col[j]: j번째 열에 경비원이 있으면 1, 없으면 0
col = [0] * M

for i in range(N):
    for j in range(M):
        if lst[i][j] == 'X':
            row[i] = 1
            col[j] = 1

# 행, 열 각각에 경비원이 몇 명이나 없는지 확인
row_cnt = row.count(0)
col_cnt = col.count(0)

# 어느 한 칸에 경비원을 배치하면 행과 열 하나씩 채울 수 있기 때문에,
# 둘 중 더 많은 수를 만족시키면 모든 행과 열을 경비원의 감시 하에 둘 수 있음
print(max(row_cnt, col_cnt))