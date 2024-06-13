import heapq
import sys
input = sys.stdin.readline

N = int(input())
q = []

for n in range(N):
    c, s = map(int, input().split())
    heapq.heappush(q, (s, c, n))

memo = [0] * (N + 1)
total = 0
result = [0] * N
now = 0
cnt = []

for n in range(N):
    s, c, n = heapq.heappop(q)
    memo[c] += s
    total += s

    if now < s:
        now = s
        cnt = [c]
    else:
        cnt.append(c)

    result[n] = total - memo[c] - s * (len(cnt) - cnt.count(c))

for n in range(N):
    print(result[n])