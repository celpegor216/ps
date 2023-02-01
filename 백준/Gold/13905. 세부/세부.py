# 힌트: 최소 신장 트리(최소 연결 부분 그래프 중 간선들의 가중치 합이 최소인 트리)
# 해답: https://velog.io/@heyksw/Python-%EB%B0%B1%EC%A4%80-13905%EB%B2%88%EC%9D%98-3%EA%B0%80%EC%A7%80-%ED%92%80%EC%9D%B4-%EB%B0%A9%EB%B2%95

from collections import deque

N, M = map(int, input().split())
S, E = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(M)]

# 최대 무게를 알아야 하기 때문에 무게제한의 부호를 바꾸어 정렬
edges.sort(key=lambda x: -x[2])

group = [n for n in range(N + 1)]    # 연결 상태 확인
tree = [[] for _ in range(N + 1)]    # 신장 트리 체크

def findboss(a):
    if group[a] == a:
        return a
    group[a] = findboss(group[a])
    return group[a]

def union(x, y):
    x_boss, y_boss = findboss(x), findboss(y)
    if x_boss != y_boss:
        group[max(x_boss, y_boss)] = min(x_boss, y_boss)

for edge in edges:
    if findboss(edge[0]) == findboss(edge[1]):
        continue
    union(edge[0], edge[1])
    tree[edge[0]].append((edge[1], edge[2]))
    tree[edge[1]].append((edge[0], edge[2]))

answer = 0

def bfs():
    global answer
    
    q = deque()
    q.append((S, 10e8))
    
    used = [0] * (N + 1)
    used[S] = 1
    
    while q:
        nowp, nowc = q.popleft()
        
        if nowp == E:
            answer = nowc
            return
        
        for p, c in tree[nowp]:
            if not used[p]:
                nowc = min(nowc, c)
                used[p] = 1
                q.append((p, nowc))

bfs()

print(answer)