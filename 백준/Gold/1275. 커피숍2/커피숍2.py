N, Q = map(int, input().split())
lst = list(map(int, input().split()))

tree = [0] * N * 4

def make_tree(idx, start, end, target):
    if start <= target <= end:
        if start == target == end:
            tree[idx] = lst[target]
        else:
            middle = (start + end) // 2

            tree[idx] = make_tree(idx * 2, start, middle, target) + make_tree(idx * 2 + 1, middle + 1, end, target)

    return tree[idx]

def find_tree(idx, start, end, target_start, target_end):
    if start > target_end or end < target_start:
        return 0
    
    if target_start <= start and end <= target_end:
        return tree[idx]

    middle = (start + end) // 2
    
    return find_tree(idx * 2, start, middle, target_start, target_end) + find_tree(idx * 2 + 1, middle + 1, end, target_start, target_end)

for n in range(N):
    make_tree(1, 0, N - 1, n)

for q in range(Q):
    x, y, a, b = map(int, input().split())

    if x < y:
        print(find_tree(1, 0, N - 1, x - 1, y - 1))
    else:
        print(find_tree(1, 0, N - 1, y - 1, x - 1))
    lst[a - 1] = b
    make_tree(1, 0, N - 1, a - 1)