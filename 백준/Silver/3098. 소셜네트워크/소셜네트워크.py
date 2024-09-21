N, M = map(int, input().split())
lst = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    lst[a][b] = 1
    lst[b][a] = 1

result = []

while 1:
    new_relationships = []

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j or not lst[i][j]:
                continue

            for k in range(1, N + 1):
                if i == k or k == j or lst[i][k] or not lst[j][k]:
                    continue

                tmp = sorted((i, k))
                if tmp in new_relationships:
                    continue
                
                new_relationships.append(tmp)
    
    if not new_relationships:
        break

    result.append(len(new_relationships))
    for a, b in new_relationships:
        lst[a][b] = 1
        lst[b][a] = 1

print(len(result))
for item in result:
    print(item)