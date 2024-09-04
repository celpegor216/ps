# 반례 참고
# 노드가 50000개라서 parents 배열의 열 크기를 무조건 16으로 하는 게 메모리 초과 원인인듯
# parents 배열 크기 줄여도 메모리 초과네...
# 해답: https://konkukcodekat.tistory.com/116


from collections import deque
import sys
input = sys.stdin.readline


N = int(input())

lst = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

# parents[i][j]: i에서 2 ** j번 거슬러 올라간 부모노드
parents = [0] * (N + 1)
# 루트는 1번
parents[1] = 1
levels = [0] * (N + 1)

q = deque()
q.append(1)

while q:
    now = q.popleft()
    for nxt in lst[now]:
        if not parents[nxt]:
            parents[nxt] = now
            levels[nxt] = levels[now] + 1
            q.append(nxt)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())

    # a의 레벨이 더 크게
    if levels[a] < levels[b]:
        a, b = b, a

    # a가 b와 레벨이 같아지도록 끌어 올리기
    while levels[a] != levels[b]:
        a = parents[a]

    # 공통 조상 찾기
    while a != b:
        a = parents[a]
        b = parents[b]

    print(a)