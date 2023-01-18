N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

for i in range(N):
    for j in range(N):
        if lst[i][j] == 1:
            houses.append((i, j))
        elif lst[i][j] == 2:
            chickens.append((i, j))
            
#     \ 치킨집
#  집

houses_length = len(houses)
chickens_length = len(chickens)
delete_length = chickens_length - M

distances = [[] for _ in range(houses_length)]

for i in range(houses_length):
    for chicken in chickens:
        distances[i].append(abs(houses[i][0] - chicken[0]) + abs(houses[i][1] - chicken[1]))

min_v = 10e8
used = [0] * chickens_length

def dfs(level, now):
    global min_v
    
    if level == delete_length:
        total = 0
        for distance in distances:
            temp = 10e8
            for i in range(chickens_length):
                if not used[i] and distance[i] < temp:
                    temp = distance[i]
            total += temp
        if total < min_v:
            min_v = total
        return

    for i in range(now, chickens_length):
        if not used[i]:
            used[i] = 1
            dfs(level + 1, i)
            used[i] = 0

dfs(0, 0)

print(min_v)