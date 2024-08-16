import heapq, sys
input = sys.stdin.readline

N = int(input())
M = int(input())
lst = [[] for _ in range(N + 1)]    # 도시의 번호가 1부터 N까지이므로 N + 1

for _ in range(M):
    a, b, c = map(int, input().split())
    lst[a].append((b, c))    # 양방향이 아닌 단방향 그래프

S, E = map(int, input().split())

q = []
heapq.heappush(q, (0, S))

# 출발부터 도착까지 모든 도시를 거쳐서 간다고 해도 1000(도시 개수)*100000(최대 비용)
# 따라서 최대값을 21 * 10 ** 8으로 지정하면 안전함
results = [int(21e8)] * (N + 1)
results[S] = 0

while q:
    cost, via = heapq.heappop(q)
    
    if results[via] < cost:
        continue

    for nxt, nxt_cost in lst[via]:
        if results[nxt] > cost + nxt_cost:
            results[nxt] = cost + nxt_cost
            heapq.heappush(q, (cost + nxt_cost, nxt))

# 출발점에서 도착점을 갈 수 있는 경우만 주어지므로 도달 가능 여부를 확인하지 않아도 됨
print(results[E])