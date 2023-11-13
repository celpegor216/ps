# 우선순위 큐를 쓰는 건 알겠는데 시간 초과를 해결 못 함
# 해답: https://hongcoding.tistory.com/79

# 넣으려는 항목의 시작 시간이 5이고
# 큐에 들어있는 항목의 종료 시간이 1, 2, 3 일 때
# 3에 넣는 게 맞을 거라고 생각을 했는데,
# 이미 넣으려는 항목이 정렬되어 있으니까
# 지금 넣으려는 항목 이후의 시작 시간이 어차피 지금보다 크거나 같을 것이므로
# 큐의 맨 앞만 확인하면 됨

import heapq
import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()

q = []
heapq.heappush(q, lst[0][1])

for n in range(1, N):
    if lst[n][0] >= q[0]:
        heapq.heappop(q)
    heapq.heappush(q, lst[n][1])

print(len(q))