from collections import deque


def solution(board):
    N, M = len(board), len(board[0])
    answer = -1
    used = [[0] * M for _ in range(N)]

    q = deque()

    for n in range(N):
        for m in range(M):
            if board[n][m] == 'R':
                q.append((n, m, 0))
                used[n][m] = 1
                break

    while q:
        nowy, nowx, nowc = q.popleft()

        if board[nowy][nowx] == 'G':
            answer = nowc
            break

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = nowy + dy, nowx + dx
            while 0 <= ny < N and 0 <= nx < M:
                if board[ny][nx] != 'D':
                    ny += dy
                    nx += dx
                else:
                    ny -= dy
                    nx -= dx
                    break
            
            if not(0 <= ny < N and 0 <= nx < M):
                ny -= dy
                nx -= dx

            if not used[ny][nx]:
                used[ny][nx] = nowc + 1
                q.append((ny, nx, nowc + 1))
    
    return answer