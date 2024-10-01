# 원산지가 잡히는 경우를 처리하지 못했음


N, M = map(int, input().split())
parent = [0] * N
children = [[] for _ in range(N)]

transform = lambda x: ord(x) - ord('A')

for _ in range(M):
    a, b = map(transform, input().split())
    parent[b] += 1
    children[a].append(b)

_, *caught = input().split()
caught = list(map(transform, caught))

q = []
for i in range(N):
    if not parent[i] and children[i] and i not in caught:
        q.append(i)

result = [0] * N

while q:
    nq = []

    for now in q:
        for child in children[now]:
            if result[child] or child in caught:
                continue

            result[child] = 1
            nq.append(child)

    q = nq

print(sum(result))