N = int(input())

lst = [[] for _ in range(3)]
buckets = [[0] * 101 for _ in range(3)]

for _ in range(N):
    tmp = list(map(int, input().split()))

    for j in range(3):
        lst[j].append(tmp[j])
        buckets[j][tmp[j]] += 1

result = [0] * N
for i in range(N):
    for j in range(3):
        if buckets[j][lst[j][i]] == 1:
            result[i] += lst[j][i]

print(*result, sep='\n')