N = int(input())

tree = [[] for _ in range(N + 1)]

for n in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

Q = int(input())

for q in range(Q):
    t, k = map(int, input().split())

    result = 'yes'
    if t == 1 and len(tree[k]) == 1:
        result = 'no'
    
    print(result)