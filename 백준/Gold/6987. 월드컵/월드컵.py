# 가능한 경우의 수를 모두 구해놓고 그 안에 있는지 찾는 방식으로 하려고 했는데
# 가능한 경우의 수가 3 ** 15라서 시간초과가 나는 것 같음
# 브루트포스가 아닌가? 조건문으로 처리하기에는 조건이 너무 복잡해질 것 같은데
# 힌트: 브루트포스, 백트래킹

lst = [[] for _ in range(4)]

for n in range(4):
    tmp = list(map(int, input().split()))
    
    for m in range(6):
        lst[n].append(tmp[3 * m:3 * (m + 1)])

vs = []
for i in range(5):
    for j in range(i + 1, 6):
        vs.append([i, j])

def dfs(level, scores):
    global result

    if result:
        return

    if level == 15:
        result = 1
        return
    
    if scores[vs[level][0]][0] > 0 and scores[vs[level][1]][2] > 0:
        scores[vs[level][0]][0] -= 1
        scores[vs[level][1]][2] -= 1
        dfs(level + 1, scores)
        scores[vs[level][0]][0] += 1
        scores[vs[level][1]][2] += 1

    if scores[vs[level][0]][2] > 0 and scores[vs[level][1]][0] > 0:
        scores[vs[level][0]][2] -= 1
        scores[vs[level][1]][0] -= 1
        dfs(level + 1, scores)
        scores[vs[level][0]][2] += 1
        scores[vs[level][1]][0] += 1

    if scores[vs[level][0]][1] > 0 and scores[vs[level][1]][1] > 0:
        scores[vs[level][0]][1] -= 1
        scores[vs[level][1]][1] -= 1
        dfs(level + 1, scores)
        scores[vs[level][0]][1] += 1
        scores[vs[level][1]][1] += 1

for n in range(4):
    result = 0

    if sum([sum(item) for item in lst[n]]) == 30:
        dfs(0, lst[n])

    print(result, end=' ')