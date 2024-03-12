import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [int(input()) for _ in range(N)]
tree = [0] * (N * 4)

def make_tree(idx, start, end):
    if start == end:
        tree[idx] = lst[start]
        return tree[idx]

    middle = (start + end) // 2

    left = make_tree(idx * 2, start, middle)
    right = make_tree(idx * 2 + 1, middle + 1, end)

    tree[idx] = min(left, right)
    return tree[idx]

make_tree(1, 0, N - 1)

def find_tree(idx, start, end, left, right):
    if start > right or end < left:
        return 21e10
    
    if start <= left and right <= end:
        return tree[idx]
    
    middle = (left + right) // 2

    l = find_tree(idx * 2, start, end, left, middle)
    r = find_tree(idx * 2 + 1, start, end, middle + 1, right)

    return min(l, r)

for m in range(M):
    a, b = map(int, input().split())
    print(find_tree(1, a - 1, b - 1, 0, N - 1))