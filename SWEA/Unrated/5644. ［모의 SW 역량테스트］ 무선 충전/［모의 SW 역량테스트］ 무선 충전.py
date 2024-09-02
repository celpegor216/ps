from collections import deque
import heapq

TC = int(input())

N = 10
directions = ((0, 0), (-1, 0), (0, 1), (1, 0), (0, -1))


for tc in range(1, TC + 1):
    T, A = map(int, input().split())
    move_a = list(map(int, input().split()))
    move_b = list(map(int, input().split()))
    # 좌표(X, Y), 충전 범위(C), 처리량(P)
    batteries = [list(map(int, input().split())) for _ in range(A)]

    ay = ax = 0
    by = bx = N - 1

    # lst[i][j]: (i, j) 위치에서 충전할 수 있는 배터리의 인덱스
    lst = [[[] for _ in range(N)] for _ in range(N)]

    for idx, (x, y, c, p) in enumerate(batteries):
        x -= 1
        y -= 1

        q = deque()
        q.append((y, x))

        used = [[0] * N for _ in range(N)]
        used[y][x] = 1

        lst[y][x].append(idx)

        while q:
            y, x = q.popleft()

            if used[y][x] == c + 1:
                break

            for dy, dx in directions[1:]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N and not used[ny][nx]:
                    used[ny][nx] = used[y][x] + 1
                    lst[ny][nx].append(idx)
                    q.append((ny, nx))

    # 모든 사용자가 충전한 양의 합의 최댓값
    result = 0

    for t in range(T + 1):
        # 사용자의 초기 위치(0초)부터 충전을 할 수 있다.
        # BC 1과 BC 3의 충전 범위에 모두 속하기 때문에, 이 위치에서는 두 BC 중 하나를 선택하여 접속
        # 한 BC에 두 명의 사용자가 접속한 경우, 접속한 사용자의 수만큼 충전 양을 균등하게 분배

        maxv = 0
        if lst[ay][ax] and lst[by][bx]:
            for a in lst[ay][ax]:
                for b in lst[by][bx]:
                    if a == b:
                        maxv = max(maxv, batteries[a][-1])
                    else:
                        maxv = max(maxv, batteries[a][-1] + batteries[b][-1])
        elif lst[ay][ax]:
            for a in lst[ay][ax]:
                maxv = max(maxv, batteries[a][-1])
        elif lst[by][bx]:
            for b in lst[by][bx]:
                maxv = max(maxv, batteries[b][-1])
        
        result += maxv

        if t == T:
            break

        ay += directions[move_a[t]][0]
        ax += directions[move_a[t]][1]
        by += directions[move_b[t]][0]
        bx += directions[move_b[t]][1]


    print(f'#{tc} {result}')