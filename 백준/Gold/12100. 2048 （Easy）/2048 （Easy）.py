from copy import deepcopy

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

result = 0

def move(level, now):
    global result

    for i in range(N):
        for j in range(N):
            result = max(result, now[i][j])

    if level == 5:
        return
    
    up = deepcopy(now)
    used = [[0] * N for _ in range(N)]
    for j in range(N):
        for i in range(1, N):
            idx = i - 1
            while idx >= 0:
                if not up[idx][j]:
                    if idx != 0:
                        idx -= 1
                    else:
                        up[idx][j] = up[i][j]
                        up[i][j] = 0
                        break
                else:
                    if up[idx][j] == up[i][j] and not used[idx][j]:
                        used[idx][j] = 1
                        up[idx][j] *= 2
                        up[i][j] = 0
                    else:
                        if idx + 1 != i:
                            up[idx + 1][j] = up[i][j]
                            up[i][j] = 0
                    break
    
    flag = 0
    for i in range(N):
        if flag:
            break

        for j in range(N):
            if now[i][j] != up[i][j]:
                flag = 1
                break
    
    if flag:
        move(level + 1, up)
  
    down = deepcopy(now)
    used = [[0] * N for _ in range(N)]
    for j in range(N):
        for i in range(N - 2, -1, -1):
            idx = i + 1
            while idx < N:
                if not down[idx][j]:
                    if idx != N - 1:
                        idx += 1
                    else:
                        down[idx][j] = down[i][j]
                        down[i][j] = 0
                        break
                else:
                    if down[idx][j] == down[i][j] and not used[idx][j]:
                        used[idx][j] = 1
                        down[idx][j] *= 2
                        down[i][j] = 0
                    else:
                        if idx - 1 != i:
                            down[idx - 1][j] = down[i][j]
                            down[i][j] = 0
                    break
    
    flag = 0
    for i in range(N):
        if flag:
            break

        for j in range(N):
            if now[i][j] != down[i][j]:
                flag = 1
                break
    
    if flag:
        move(level + 1, down)
  
    left = deepcopy(now)
    used = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(1, N):
            idx = j - 1
            while idx >= 0:
                if not left[i][idx]:
                    if idx != 0:
                        idx -= 1
                    else:
                        left[i][idx] = left[i][j]
                        left[i][j] = 0
                        break
                else:
                    if left[i][idx] == left[i][j] and not used[i][idx]:
                        used[i][idx] = 1
                        left[i][idx] *= 2
                        left[i][j] = 0
                    else:
                        if idx + 1 != j:
                            left[i][idx + 1] = left[i][j]
                            left[i][j] = 0
                    break
    
    flag = 0
    for i in range(N):
        if flag:
            break

        for j in range(N):
            if now[i][j] != left[i][j]:
                flag = 1
                break
    
    if flag:
        move(level + 1, left)
  
    right = deepcopy(now)
    used = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N - 2, -1, -1):
            idx = j + 1
            while idx < N:
                if not right[i][idx]:
                    if idx != N - 1:
                        idx += 1
                    else:
                        right[i][idx] = right[i][j]
                        right[i][j] = 0
                        break
                else:
                    if right[i][idx] == right[i][j] and not used[i][idx]:
                        used[i][idx] = 1
                        right[i][idx] *= 2
                        right[i][j] = 0
                    else:
                        if idx - 1 != j:
                            right[i][idx - 1] = right[i][j]
                            right[i][j] = 0
                    break
    
    flag = 0
    for i in range(N):
        if flag:
            break

        for j in range(N):
            if now[i][j] != right[i][j]:
                flag = 1
                break
    
    if flag:
        move(level + 1, right)


move(0, lst)

print(result)