# 최대 유량이라는 알고리즘이 있구나,,,
# 해답: https://sosoeasy.tistory.com/311


from collections import deque


N = 52
S = 0
E = 25
M = int(input())

def char_to_num(x):
    if x.islower():
        return ord(x) - ord('a') + 26
    else:
        return ord(x) - ord('A')

cost = [[0] * N for _ in range(N)]    # a와 b 사이 파이프 용량
graph = [[] for _ in range(N)]    # a와 연결된 노드들
flow = [[0] * N for _ in range(N)]    # a와 연결된 간선의 최대 값
for _ in range(M):
    a, b, c = input().split()
    a = char_to_num(a)
    b = char_to_num(b)
    c = int(c)

    cost[a][b] += c
    cost[b][a] += c
    graph[a].append(b)
    graph[b].append(a)


result = 0
while 1:
    # A에서 Z까지 가능한 경로 찾기
    prev = [-1] * N
    q = deque([S])

    while q:
        now = q.popleft()

        if now == E:
            break

        for nxt in graph[now]:
            # 현재의 flow가 해당 간선의 최대 flow를 넘지 않고, 방문하지 않았다면
            if cost[now][nxt] - flow[now][nxt] > 0 and prev[nxt] == -1:
                q.append(nxt)
                prev[nxt] = now

    # A에서 Z까지 가능한 경로가 더이상 없는 경우
    if prev[E] == -1:
        break

    min_flow = 21e8

    # A에서 Z로 가는 경로의 최소 용량 찾기
    now = E
    while now != S:
        rest = cost[prev[now]][now] - flow[prev[now]][now]
        min_flow = min(min_flow, rest)
        now = prev[now]

    # 경로의 최소 용량으로 업데이트
    now = E
    while now != S:
        flow[prev[now]][now] += min_flow
        flow[now][prev[now]] -= min_flow
        now = prev[now]

    result += min_flow

print(result)