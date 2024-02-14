# 세그먼트 트리
# 시간 초과 -> 매번 트리를 생성하지 않고 미리 트리를 만들어둬야함
# 해답: https://squareyun.tistory.com/103

import math
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [int(input()) for _ in range(N)]

h = math.ceil(math.log2(N)) + 1
memo = [0] * (1 << h)

def segment_tree(idx, left, right):
    if left == right:
        memo[idx] = (lst[left], lst[left])
    else:
        middle = (left + right) // 2

        tmpl = segment_tree(idx * 2, left, middle)
        tmpr = segment_tree(idx * 2 + 1, middle + 1, right)

        memo[idx] = (min(tmpl[0], tmpr[0]), max(tmpl[1], tmpr[1]))
    return memo[idx]

segment_tree(1, 0, N - 1)

def find(idx, start, end, left, right):
    if start > right or end < left:
        return (10 ** 9 + 1, 0)
    
    if start <= left and right <= end:
        return memo[idx]
    
    middle = (left + right) // 2
    
    tmpl = find(idx * 2, start, end, left, middle)
    tmpr = find(idx * 2 + 1, start, end, middle + 1, right)

    return (min(tmpl[0], tmpr[0]), max(tmpl[1], tmpr[1]))

for m in range(M):
    a, b = map(int, input().split())

    print(*find(1, a - 1, b - 1, 0, N - 1))