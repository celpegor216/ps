import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

tree = [0] * N * 4

def update_tree(idx, l, r, t, v):
    if l == t == r:
        tree[idx] += v
    elif l <= t <= r:
        m = (l + r) // 2

        left = update_tree(idx * 2, l, m, t, v)
        right = update_tree(idx * 2 + 1, m + 1, r, t, v)

        tree[idx] = left + right
    return tree[idx]

def find_tree(idx, l, r, tl, tr):
    if tl > r or tr < l:
        return 0
    elif tl <= l and r <= tr:
        return tree[idx]
    else:
        m = (l + r) // 2

        left = find_tree(idx * 2, l, m, tl, tr)
        right = find_tree(idx * 2 + 1, m + 1, r, tl, tr)

        return left + right

for _ in range(Q):
    q, a, b = map(int, input().split())
    
    if q == 1:
        update_tree(1, 1, N, a, b)
    else:
        print(find_tree(1, 1, N, a, b))