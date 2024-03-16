import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]
mod = 1000000007

tree = [0] * (N * 4)

def make_tree(idx, start, end):
    if start == end:
        tree[idx] = lst[start]
    else:    
        middle = (start + end) // 2

        left = make_tree(idx * 2, start, middle)
        right = make_tree(idx * 2 + 1, middle + 1, end)

        tree[idx] = (left * right) % mod
    return tree[idx]

make_tree(1, 0, N - 1)

def update_tree(idx, start, end, target):
    if start <= target <= end:
        if start == end:
            tree[idx] = lst[start]
        else:
            middle = (start + end) // 2

            left = update_tree(idx * 2, start, middle, target)
            right = update_tree(idx * 2 + 1, middle + 1, end, target)

            tree[idx] = (left * right) % mod
    return tree[idx]

def find_tree(idx, start, end, left, right):
    if start > right or end < left:
        return 1
    
    if left <= start and end <= right:
        return tree[idx]
    
    middle = (start + end) // 2

    l = find_tree(idx * 2, start, middle, left, right)
    r = find_tree(idx * 2 + 1, middle + 1, end, left, right)

    return (l * r) % mod

for _ in range(M + K):
    a, b, c = map(int, input().split())
    b -= 1

    if a == 1:
        lst[b] = c
        update_tree(1, 0, N - 1, b)
    else:
        print(find_tree(1, 0, N - 1, b, c - 1))