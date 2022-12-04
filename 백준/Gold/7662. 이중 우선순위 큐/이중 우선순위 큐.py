# 답 봤음 https://neomindstd.github.io/%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4/boj7662/

import heapq
import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    K = int(input())

    minq = []
    maxq = []
    visited = [0] * 10000001 # id별 활성 상태 기록

    for k in range(K):
        command, num = input().split()
        num = int(num)

        if command == 'I':
            heapq.heappush(minq, (num, k)) # k는 식별자(id)
            heapq.heappush(maxq, (-num, k))
            visited[k] = 1
        else:
            if num == 1: # 최댓값 삭제
                # id를 기준으로 해당 노드가 minq에서 삭제된 노드인지 확인
                # 삭제된 경우, 삭제되지 않은 노드가 나올 때까지 모두 버림
                while maxq and not visited[maxq[0][1]]:
                    heapq.heappop(maxq)
                # 이번에 삭제해야 하는 노드가 등장하면 삭제
                if maxq:
                    visited[maxq[0][1]] = 0
                    heapq.heappop(maxq)
            else:
                while minq and not visited[minq[0][1]]:
                    heapq.heappop(minq)
                if minq:
                    visited[minq[0][1]] = 0
                    heapq.heappop(minq)

    # 삭제되어야 하는데 아직 삭제되지 않은 노드들이 있는지 확인 후 삭제
    while minq and not visited[minq[0][1]]:
        heapq.heappop(minq)
    while maxq and not visited[maxq[0][1]]:
        heapq.heappop(maxq)

    if minq and maxq:
        print(-heapq.heappop(maxq)[0], heapq.heappop(minq)[0])
    else:
        print('EMPTY')