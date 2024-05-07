# 해답: https://velog.io/@ju_h2/Python-%EB%B0%B1%EC%A4%80-1781.-%EC%BB%B5%EB%9D%BC%EB%A9%B4-%ED%92%80%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%83%90%EC%9A%95-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EA%B7%B8%EB%A6%AC%EB%94%94-%EA%B5%AC%ED%98%84-6

import heapq
import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()

q = []

for a, b in lst:
    heapq.heappush(q, b)
    if a < len(q):
        heapq.heappop(q)

print(sum(q))