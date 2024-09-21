N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
D = int(input())
directions = [list(map(int, input().split())) for _ in range(D)]


def find():
    q = []
    used = [[0] * M for _ in range(N)]
    for m in range(M):
        if lst[0][m]:
            q.append((0, m))
            used[0][m] = 1

    result = 0
    while q:
        nq = []

        for y, x in q:
            if y == N - 1:
                return result
            
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx]:
                    nq.append((ny, nx))
                    used[ny][nx] = 1
        
        q = nq
        result += 1
    
    return -1


print(find())