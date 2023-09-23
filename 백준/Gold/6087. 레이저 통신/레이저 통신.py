# bfs로 풀었는데 메모리 초과 발생...
# 가지치기 제대로 한 것 같은데 여기서 어떻게 더 줄일 수 있지?

# 해답: https://hi-guten-tag.tistory.com/425

import heapq

M, N = map(int, input().split())
lst = [list(input()) for _ in range(N)]

sy, sx = -1, -1
ey, ex = -1, -1

for n in range(N):
    for m in range(M):
        if lst[n][m] == 'C':
            if sy == -1:
                sy, sx = n, m
            else:
                ey, ex = n, m

# 거울 개수
cnt = [[21e21] * M for _ in range(N)]
cnt[sy][sx] = 0

# 방문 체크(수직/수평)
check = [[[0] * M for _ in range(N)] for _ in range(2)]

ds = ((0, 1), (1, 0), (0, -1), (-1, 0))

q = []
heapq.heappush(q, (-1, sy, sx))
lst[sy][sx] = '*'

result = -1

while q:
    nowc, nowy, nowx = heapq.heappop(q)
    nowc += 1

    for i in range(4):
        ny, nx = nowy, nowx

        if result > -1:
            break
        
        while 1:
            ny += ds[i][0]
            nx += ds[i][1]

            if 0 <= ny < N and 0 <= nx < M:
                if lst[ny][nx] == '*': break
                if lst[ny][nx] == 'C':
                    result = nowc
                    break
                
                # 기존 거울 개수보다 적거나
                # 같게 사용했더라도 수직/수평으로 방문하지 않았다면
                if cnt[ny][nx] > nowc or (cnt[ny][nx] == nowc and check[i % 2][ny][nx] == 0):
                    cnt[ny][nx] = nowc
                    check[i % 2][ny][nx] = 1

                    heapq.heappush(q, (nowc, ny, nx))
            else:
                break
    
    if result > -1:
        break

print(result)