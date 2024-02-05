import heapq
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
powers = list(map(int, input().split()))

lines = []

for m in range(M):
    u, v, w = map(int, input().split())
    heapq.heappush(lines, (w, u, v))

result = 0
group = [x for x in range(N + 1)]

def find(a):
    if group[a] != a:
        group[a] = find(group[a])
    return group[a]

def union(a, b, c):
    global result

    group_a, group_b = find(a), find(b)

    is_a_power = group_a in powers
    is_b_power = group_b in powers

    if group_a != group_b:
        if not(is_a_power or is_b_power) or (is_a_power and not is_b_power):
            group[group_b] = group_a
            result += c
        elif is_b_power and not is_a_power:
            group[group_a] = group_b
            result += c

for m in range(M):
    c, a, b = heapq.heappop(lines)
    union(a, b, c)

print(result)