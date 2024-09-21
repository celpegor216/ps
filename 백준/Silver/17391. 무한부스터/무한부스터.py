N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

def find():
    q = []
    q.append((0, 0))

    used = [[0] * M for _ in range(N)]
    used[0][0] = 1

    result = 0
    while q:
        nq = []

        for y, x in q:
            if y == N - 1 and x == M - 1:
                return result
            
            for i in range(1, lst[y][x] + 1):
                nx = x + i
                if 0 <= nx < M and not used[y][nx]:
                    used[y][nx] = 1
                    nq.append((y, nx))
                
                ny = y + i
                if 0 <= ny < N and not used[ny][x]:
                    used[ny][x] = 1
                    nq.append((ny, x))
                
        q = nq
        result += 1


print(find())