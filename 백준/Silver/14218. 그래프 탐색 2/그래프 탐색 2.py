import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())

lst = [[] for _ in range(N)]

def transform(x):
    return int(x) - 1

for _ in range(M):
    a, b = map(transform, input().split())
    lst[a].append(b)
    lst[b].append(a)


def dijkstra():
    # 수도는 1번도시
    result = [-1] * N
    result[0] = 0

    q = []
    heapq.heappush(q, (0, 0))

    while q:
        cost, via = heapq.heappop(q)

        for nxt in lst[via]:
            if result[nxt] == -1 or result[nxt] > cost + 1:
                result[nxt] = cost + 1
                heapq.heappush(q, (cost + 1, nxt))
    
    return result

Q = int(input())
for _ in range(Q):
    a, b = map(transform, input().split())
    lst[a].append(b)
    lst[b].append(a)
    print(*dijkstra())