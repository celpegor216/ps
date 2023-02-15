lst = [list(map(int, input().split())) for _ in range(19)]

answer = []

def solution():
    global answer
    for i in range(19):
        for j in range(19):
            if lst[i][j]:
                for dy, dx in ((0, 1), (1, 0), (1, 1), (-1, 1)):
                    ny, nx = i - dy, j - dx
                    if not (0 <= ny < 19 and 0 <= nx < 19) or (0 <= ny < 19 and 0 <= nx < 19 and lst[ny][nx] != lst[i][j]):
                        ny, nx = i + dy, j + dx
                        flag = 0
                        for k in range(4):
                            if 0 <= ny < 19 and 0 <= nx < 19:
                                if lst[ny][nx] != lst[i][j]:
                                    flag = 1
                                    break
                                ny += dy
                                nx += dx
                            else:
                                flag = 1
                                break
                        if not flag and (not (0 <= ny < 19 and 0 <= nx < 19) or ( 0 <= ny < 19 and 0 <= nx < 19 and lst[ny][nx] != lst[i][j])):
                            answer = [i, j]
                            return

solution()

if not answer:
    print(0)
else:
    print(lst[answer[0]][answer[1]])
    print(answer[0] + 1, answer[1] + 1)