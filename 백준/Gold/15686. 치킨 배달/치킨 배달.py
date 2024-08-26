# 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램
# m이 최대 13이므로 dfs를 돌려서 조합을 만든 다음 계산하면 될 것 같다

N, M = map(int, input().split())
# 크기가 N×N인 도시
# 0은 빈 칸, 1은 집, 2는 치킨집
lst = [list(map(int, input().split())) for _ in range(N)]


chickens = []
people = []
for i in range(N):
    for j in range(N):
        if lst[i][j] == 2:
            chickens.append((i, j))
        elif lst[i][j] == 1:
            people.append((i, j))

P = len(people)
C = len(chickens)
# distances[i][j]: 사람 i부터 치킨집 j까지의 거리
distances = [[0] * C for _ in range(P)]

for p in range(P):
    for c in range(C):
        distances[p][c] = abs(people[p][0] - chickens[c][0]) + abs(people[p][1] - chickens[c][1])

# 최대 값은 전체 배열 크기 * 사람 수
result = N ** 2 * 2 * N
used = [0] * C
def dfs(level, start, selected_chickens):
    global result

    if level == M:
        total = 0

        for p in range(P):
            minv = N ** 2
            for c in selected_chickens:
                minv = min(minv, distances[p][c])
            total += minv

        result = min(result, total)
        return

    for c in range(start, C):
        if not used[c]:
            used[c] = 1
            dfs(level + 1, c + 1, selected_chickens + [c])
            used[c] = 0

dfs(0, 0, [])

print(result)