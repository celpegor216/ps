# 해답: https://konkukcodekat.tistory.com/111

from collections import deque

N, S, E, M = map(int, input().split())
lst = []

for _ in range(M):
    a, b, c = map(int, input().split())
    lst.append([a, b, -c])

costs = list(map(int, input().split()))

for m in range(M):
    lst[m][2] += costs[lst[m][1]]

# 벨만 포드: 사이클 확인 가능
def bf():
    INF = -21e10

    result = [INF] * N
    result[S] = costs[S]

    for _ in range(N - 1):
        for a, b, c in lst:
            if result[a] != INF and result[a] + c > result[b]:
                result[b] = result[a] + c
    
    if result[E] == INF:
        return 'gg'

    # 사이클 확인 + 사이클에서 E로 갈 수 있는지 확인
    for a, b, c in lst:
        if result[a] != INF and result[a] + c > result[b]:
            flag = 0
            
            q = deque()
            q.append(a)
            used = [0] * N
            used[a] = 1

            while q:
                now = q.popleft()

                if now == E:
                    flag = 1
                    break
                    
                for A, B, _ in lst:
                    if now == A and not used[B]:
                        used[B] = 1
                        q.append(B)
            
            if flag:
                return 'Gee'
    
    return result[E]

print(bf())