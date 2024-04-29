# 힌트: 스택
# 해답: https://hillier.tistory.com/118

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
path = [[] for _ in range(M)]

def find_path(y, x, m):
    while 1:
        path[m].append((y, x))
        if y + 1 == N or board[y + 1][x] == 'X':
            return
        if board[y + 1][x] == 'O':
            if 0 <= x - 1 and board[y][x - 1] == '.' and board[y + 1][x - 1] == '.':
                x -= 1
            elif x + 1 < M and board[y][x + 1] == '.' and board[y + 1][x + 1] == '.':
                x += 1
            else:
                return
        y += 1

Q = int(input())
for _ in range(Q):
    m = int(input()) - 1

    while path[m]:
        y, x = path[m][-1]
        if board[y][x] == '.':
            break
        path[m].pop()
    
    if path[m]:
        y, x = path[m].pop()
        find_path(y, x, m)
    else:
        find_path(0, m, m)

    y, x = path[m].pop()
    board[y][x] = 'O'

for line in board:
    print(''.join(line))