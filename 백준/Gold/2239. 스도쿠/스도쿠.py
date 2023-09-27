# 접근법은 맞았는데 시간초과
# 해답: https://hazung.tistory.com/153

lst = [list(map(int, list(input()))) for _ in range(9)]
used_row = [[0] * 10 for _ in range(9)]
used_col = [[0] * 10 for _ in range(9)]
used_block = [[0] * 10 for _ in range(9)]

for i in range(9):
    for j in range(9):
        used_row[i][lst[i][j]] = 1
        used_col[j][lst[i][j]] = 1
        used_block[(i // 3) * 3 + (j // 3)][lst[i][j]] = 1

result = []
def dfs(n):
    if n == 81:
        for line in lst:
            print(''.join(map(str, line)))
        return 1
    
    i, j = n // 9, n % 9

    if lst[i][j]: return dfs(n + 1)
    else:    
        for num in range(1, 10):
            if not used_row[i][num] and not used_col[j][num] and not used_block[(i // 3) * 3 + (j // 3)][num]:
                lst[i][j] = num
                used_row[i][num] = 1
                used_col[j][num] = 1
                used_block[(i // 3) * 3 + (j // 3)][num] = 1
                
                if dfs(n + 1): return 1
                
                lst[i][j] = 0
                used_row[i][num] = 0
                used_col[j][num] = 0
                used_block[(i // 3) * 3 + (j // 3)][num] = 0
    
    return 0

dfs(0)