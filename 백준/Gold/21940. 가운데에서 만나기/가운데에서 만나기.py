# 두 번째 예제가 어떻게 1, 2, 3이지? 1, 2 아닌가? 문제가 이해되지 않음
# 해답: https://velog.io/@isayaksh/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-BOJ-21940-%EA%B0%80%EC%9A%B4%EB%8D%B0%EC%97%90%EC%84%9C-%EB%A7%8C%EB%82%98%EA%B8%B0-Python
# 준형이와 친구들의 왕복시간들 중 최대가 최소가 되는 도시

N, M = map(int, input().split())
table = [[21e8] * (N + 1) for _ in range(N + 1)]

for m in range(M):
    a, b, c = map(int, input().split())
    table[a][b] = c

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            table[i][j] = min(table[i][j], table[i][k] + table[k][j])

K = int(input())
cities = list(map(int, input().split()))

for n in range(1, N + 1):
    table[n][n] = 0 

maxvs = [0] * (N + 1)
for n in range(1, N + 1):
    v = 0
    for city in cities:
        v = max(v, table[city][n] + table[n][city])
    
    maxvs[n] = v

resultv = min(maxvs[1:])
resultx = []

for n in range(1, N + 1):
    if maxvs[n] == resultv:
        resultx.append(n)

print(*sorted(resultx))