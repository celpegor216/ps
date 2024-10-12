# 해답: https://hseungyeon.tistory.com/239


import sys
input = sys.stdin.readline


N, M, K = map(int, input().split())
lst = [list(input()) for _ in range(N)]
sy, sx, ey, ex = map(lambda x: int(x) - 1, input().split())

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))


def find(sy, sx, ey, ex):
    q = [(sy, sx)]
    lst[sy][sx] = 0

    while q:
        nq = []

        for y, x in q:
            if y == ey and x == ex:
                return lst[y][x]
            
            for dy, dx in directions:
                for k in range(1, K + 1):
                    ny, nx = y + dy * k, x + dx * k
                    if not (0 <= ny < N and 0 <= nx < M) or lst[ny][nx] == '#':
                        break
                    
                    # 방문하지 않은 길이면 방문 처리
                    if lst[ny][nx] == '.':
                        lst[ny][nx] = lst[y][x] + 1
                        nq.append((ny, nx))
                    
                    # 방문했는데 지금보다 값이 더 크다면 그냥 계속 탐색
                    elif lst[ny][nx] > lst[y][x]:
                        continue
                    
                    # 방문했는데 지금보다 값이 더 작거나 지금과 같다면 중단
                    else:
                        break
        
        q = nq

    return -1


print(find(sy, sx, ey, ex))