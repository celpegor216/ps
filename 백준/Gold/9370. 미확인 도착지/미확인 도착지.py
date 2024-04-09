# 메모리 초과
# 해답: https://cobokjang.tistory.com/16

from collections import deque
import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M, T = map(int, input().split())
    S, G, H = map(int, input().split())
    lst = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, d = map(int, input().split())
        lst[a].append((b, d))
        lst[b].append((a, d))
    targets = [int(input()) for _ in range(T)]
    targets.sort()

    tmp_cost = [21e8] * (N + 1)
    tmp_flag = [0] * (N + 1)

    q = []
    heapq.heappush(q, (0, 0, S))

    while q:
        now_cost, flag, now = heapq.heappop(q)

        # 같은 cost일 때 flag 값이 적으면 먼저 선택되므로 같은 값도 쳐냄
        if tmp_cost[now] <= now_cost:
            continue

        tmp_cost[now] = now_cost
        tmp_flag[now] = flag

        for item, cost in lst[now]:
            new_cost = now_cost + cost
            if tmp_cost[item] >= new_cost:
                if (now == H and item == G) or (now == G and item == H):
                    heapq.heappush(q, (new_cost, -1, item))
                else:
                    heapq.heappush(q, (new_cost, flag, item))

    for target in targets:
        if tmp_flag[target] == -1:
            print(target, end = ' ')

    print()
