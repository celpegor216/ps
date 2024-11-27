import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [int(input()) for _ in range(N)]

min_tree = [0] * 4 * N
max_tree = [0] * 4 * N


def update_tree(tree_idx, start, end):
    if not min_tree[tree_idx] or not max_tree[tree_idx]:
        # 리프 노드까지 내려온 경우
        if start == end:
            min_tree[tree_idx] = lst[start]
            max_tree[tree_idx] = lst[start]
        else:
            middle = (start + end) // 2

            left = update_tree(tree_idx * 2, start, middle)
            right = update_tree(tree_idx * 2 + 1, middle + 1, end)

            min_tree[tree_idx] = min(left[0], right[0])
            max_tree[tree_idx] = max(left[1], right[1])
    return min_tree[tree_idx], max_tree[tree_idx]


update_tree(1, 0, N - 1)


def find_tree(tree_idx, target_start, target_end, now_start, now_end):
    # 현재 범위가 타겟 범위를 벗어난 경우
    if target_end < now_start or now_end < target_start:
        return (21e8, -21e8)

    # 리프 노드까지 왔거나, 현재 범위가 타겟 범위 내부인 경우
    if now_start == now_end or (target_start <= now_start and now_end <= target_end):
        return min_tree[tree_idx], max_tree[tree_idx]
    
    middle = (now_start + now_end) // 2

    left = find_tree(tree_idx * 2, target_start, target_end, now_start, middle)
    right = find_tree(tree_idx * 2 + 1, target_start, target_end, middle + 1, now_end)

    return min(left[0], right[0]), max(left[1], right[1])


for _ in range(M):
    # a부터 b까지니까 a < b가 보장된듯?
    a, b = map(lambda x: int(x) - 1, input().split())

    print(*find_tree(1, a, b, 0, N - 1))
