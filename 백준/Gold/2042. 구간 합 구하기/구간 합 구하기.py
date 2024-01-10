# 해답: https://velog.io/@heyoni/2042

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]
tree = [0] * (N * 4)

# 트리 만들기
def init(start, end, idx):
    if start == end:
        tree[idx] = lst[start - 1]
    else:
        middle = (start + end) // 2
        tree[idx] = init(start, middle, idx * 2) + init(middle + 1, end, idx * 2 + 1)
    return tree[idx]

# 값 찾기
def find(start, end, idx, left, right):
    if start > right or end < left:
        return 0
    
    if left <= start and end <= right:
        return tree[idx]

    middle = (start + end) // 2
    return find(start, middle, idx * 2, left, right) + find(middle + 1, end, idx * 2 + 1, left, right)

# 값 바꾸기
def update(start, end, idx, update_idx, update_v):
    if start > update_idx or end < update_idx:
        return
    
    tree[idx] += update_v

    if start == end:
        return
    
    middle = (start + end) // 2
    update(start, middle, idx * 2, update_idx, update_v)
    update(middle + 1, end, idx * 2 + 1, update_idx, update_v)

init(1, N, 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:
        v = c - lst[b - 1]
        lst[b - 1] = c
        update(1, N, 1, b, v)
    else:
        print(find(1, N, 1, b, c))