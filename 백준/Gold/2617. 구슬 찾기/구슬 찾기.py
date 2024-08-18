N, M = map(int, input().split())

parents = [set() for _ in range(N + 1)]
children = [set() for _ in range(N + 1)]

for _ in range(M):
    p, c = map(int, input().split())
    parents[c].add(p)
    children[p].add(c)

used_parents = [0] * (N + 1)
used_children = [0] * (N + 1)

def find_parents(now):
    if not used_parents[now]:
        used_parents[now] = 1

        res = set()
        
        for parent in parents[now]:
            res = res.union(find_parents(parent))

        parents[now] = parents[now].union(res)

    return parents[now]


def find_children(now):
    if not used_children[now]:
        used_children[now] = 1

        res = set()

        for child in children[now]:
            res = res.union(find_children(child))
        
        children[now] = children[now].union(res)

    return children[now]


for i in range(1, N + 1):
    if not children[i]:
        find_parents(i)

    elif not parents[i]:
        find_children(i)

result = 0

half = N // 2

for i in range(1, N + 1):
    if len(children[i]) > half or len(parents[i]) > half:
        result += 1

print(result)