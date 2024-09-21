N, L = map(int, input().split())
lst = [input() for _ in range(N)]

candidates = [set() for _ in range(L)]

for i in range(N):
    for j in range(L):
        candidates[j].add(lst[i][j])

result = ''
def dfs(level, path, diff_cnts):
    global result

    if result:
        return

    if level == L:
        result = path
        return
    
    for c in candidates[level]:
        nxt_path = path + c
        nxt_diff_cnts = diff_cnts[:]

        flag = 0
        for n in range(N):
            if lst[n][level] != c:
                nxt_diff_cnts[n] += 1
                if nxt_diff_cnts[n] > 1:
                    flag = 1
                    break
        
        if not flag:
            dfs(level + 1, nxt_path, nxt_diff_cnts)

dfs(0, '', [0] * N)

if not result:
    result = 'CALL FRIEND'

print(result)