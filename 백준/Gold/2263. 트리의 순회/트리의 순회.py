# 이진 트리
# pre: root - left - right
# in: left - root - right
# post: left - right - root

import sys
sys.setrecursionlimit(100000)

N = int(input())
lst_in = list(map(int, input().split()))
lst_post = list(map(int, input().split()))

result = [0] * N

def find(pre_start, pre_end, in_start, in_end, post_start, post_end):
    # root
    result[pre_start] = lst_post[post_end]

    root_idx = lst_in.index(lst_post[post_end])
    left_size = root_idx - in_start

    # left
    if pre_start + 1 == pre_start + left_size:
        result[pre_start + 1] = lst_in[in_start]
    elif pre_start + 1 < pre_start + left_size:
        find(pre_start + 1, pre_start + left_size, 
            in_start, root_idx - 1, 
            post_start, post_start + left_size - 1)

    # right
    if pre_start + left_size + 1 == pre_end:
        result[pre_start + left_size + 1] = lst_in[root_idx + 1]
    elif pre_start + left_size + 1 < pre_end:
        find(pre_start + left_size + 1, pre_end, 
            root_idx + 1, in_end, 
            post_start + left_size, post_end - 1)

find(0, N - 1, 0, N - 1, 0, N - 1)
print(*result)