# 시간 초과 해결 못 함
# 해답: https://hazung.tistory.com/134

from collections import deque

N, K = map(int, input().split())

q = deque()
times = [0] * 100001    # 해당 숫자에 방문했을 때 최소 횟수
parents = [0] * 100001    # 해당 숫자에 최소 횟수로 방문했을 때 이전 노드

q.append(N)

while q:
    n = q.popleft()

    if n == K:
        print(times[n])
        
        result = []
        for i in range(times[n] + 1):
            result.append(n)
            n = parents[n]
        print(*result[::-1])
        break

    for i in (n + 1, n - 1, n * 2):
        if 0 <= i <= 100000 and times[i] == 0:
            q.append(i)
            times[i] = times[n] + 1
            parents[i] = n