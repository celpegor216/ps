# 반례 참고 > 했는데 해결 못 함
# 해답: https://puleugo.tistory.com/85


from collections import deque

N, M, P = map(int, input().split())
moves = list(map(int, input().split()))
lst = [list(input()) for _ in range(N)]

result = [0] * P
qs = [deque() for _ in range(P)]

for i in range(N):
    for j in range(M):
        if lst[i][j].isdigit():
            p = int(lst[i][j]) - 1
            result[p] += 1
            qs[p].append((i, j))

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

flag = 1   # 하나라도 퍼져 나간 경우 다음 사이클을 돌아야 함
while flag:
    flag = 0

    for p in range(P):
        if not qs[p]:
            continue

        for move in range(moves[p]):
            if not qs[p]:
                break

            for _ in range(len(qs[p])):
                y, x = qs[p].popleft()

                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] == '.':
                        lst[ny][nx] = '#'    # 방문 처리
                        result[p] += 1
                        qs[p].append((ny, nx))
                        flag = 1

print(*result)