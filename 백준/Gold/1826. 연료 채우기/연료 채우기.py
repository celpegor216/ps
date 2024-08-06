# bfs는 메모리 초과인데 다른 방법이 생각나지 않음
# 해답: https://lcyking.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-1826-%EC%97%B0%EB%A3%8C%EC%B1%84%EC%9A%B0%EA%B8%B0

import sys, heapq
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
L, P = map(int, input().split())    # 도착지, 초기 이동 가능한 칸 수

lst.append([L, 0])
lst.sort()    # 거리 순으로 정렬
q = []    # 넣지 않고 킵해둔 연료

result = 0
for n in range(N + 1):
    # 지금 남은 연료로 이동할 수 없는 경우 지금까지 안 넣었던 연료들 중 큰 순서대로 넣기
    while q and P < lst[n][0]:
        P += -heapq.heappop(q)
        result += 1

    # 연료를 다 넣었는데도 갈 수 없다면 종료
    if not q and P < lst[n][0]:
        result = -1
        break
    # 연료 킵
    else:
        heapq.heappush(q, -lst[n][1])

print(result)