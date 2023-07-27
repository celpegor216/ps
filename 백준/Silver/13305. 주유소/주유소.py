N = int(input())
edges = list(map(int, input().split())) # N - 1개
nodes = list(map(int, input().split())) # 마지막은 의미 없음

total = 0
nown = nodes[0]
sume = edges[0]
for n in range(1, N - 1):
    if nown <= nodes[n]:
        sume += edges[n]
    else:
        total += nown * sume
        nown = nodes[n]
        sume = edges[n]

    if n == N - 2:
        total += nown * sume

print(total)