# 세그먼트 트리로 시도했으나 시간초과
# 해답: https://codio.tistory.com/entry/%EB%B0%B1%EC%A4%80-11003%EB%B2%88-%EC%B5%9C%EC%86%9F%EA%B0%92-%EC%B0%BE%EA%B8%B0-Python%ED%8C%8C%EC%9D%B4%EC%8D%AC

from collections import deque

N, L = map(int, input().split())
lst = list(map(int, input().split()))

q = deque()

for n in range(N):
    # 맨 앞 원소 삭제
    if q and q[0][0] <= n - L:
        q.popleft()

    # 기존 원소가 들어올 원소보다 크면 삭제
    while q and q[-1][1] > lst[n]:
        q.pop()
    
    q.append((n, lst[n]))

    print(q[0][1], end=' ')