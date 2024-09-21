N = int(input())
M = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
X = int(input())


# 맨해튼 거리가 X 이하인 마스크 만들기
mask = set()

def make_mask():
    mask.add((0, 0))

    q = [(0, 0)]

    idx = 0
    for _ in range(X):
        length = len(q)
        while idx < length:
            y, x = q[idx]
            
            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ny, nx = y + dy, x + dx
                if (ny, nx) not in mask:
                    mask.add((ny, nx))
                    q.append((ny, nx))
        
            idx += 1


make_mask()


def find():
    q = [(0, 0)]
    used = [[0] * M for _ in range(N)]

    while q:
        nq = []

        for y, x in q:
            if y == N - 1 and x == M - 1:
                return 'ALIVE'
            
            for dy, dx in mask:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] == lst[0][0]:
                    used[ny][nx] = 1
                    nq.append((ny, nx))
        
        q = nq
    
    return 'DEAD'


print(find())