N = int(input())
lst = [0] + list(map(int, input().split()))

MAXV = 21e10
tree = [[MAXV, MAXV] for _ in range(4 * N)]

def update_tree(idx, s, e, t):
    if s == e == t:
        tree[idx] = [lst[t], t]
    elif s <= t <= e:
        m = (s + e) // 2

        left = update_tree(idx * 2, s, m, t)
        right = update_tree(idx * 2 + 1, m + 1, e, t)

        if left[0] < right[0] or (left[0] == right[0] and left[1] < right[1]):
            tree[idx] = left
        else:
            tree[idx] = right

    return tree[idx]

def find_tree(idx, s, e, tl, tr):
    if tl <= s and e <= tr:
        return tree[idx]
    elif s > tr or e < tl:
        return [MAXV, MAXV]
    else:
        m = (s + e) // 2

        left = find_tree(idx * 2, s, m, tl, tr)
        right = find_tree(idx * 2 + 1, m + 1, e, tl, tr)

        if left[0] < right[0] or (left[0] == right[0] and left[1] < right[1]):
            return left
        else:
            return right

for n in range(1, N + 1):
    update_tree(1, 1, N, n)

M = int(input())
for _ in range(M):
    q, a, b = map(int, input().split())

    if q == 1:
        lst[a] = b
        update_tree(1, 1, N, a)
    else:
        print(find_tree(1, 1, N, a, b)[1])