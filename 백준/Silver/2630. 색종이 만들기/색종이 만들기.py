N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]

cnt_one = 0
cnt_zero = 0

def check(x, y, num):
    global cnt_one, cnt_zero

    start = lst[x][y]

    if num == 1:
        if start == 1:
            cnt_one += 1
        else:
            cnt_zero += 1
        return
    else:
        for i in range(num):
            for j in range(num):
                if lst[x+i][y+j] != start:
                    next = num // 2
                    for k in range(2):
                        for l in range(2):
                            check(x+(next*k), y+(next*l), next)
                    return

        if start == 1:
            cnt_one += 1
        else:
            cnt_zero += 1

check(0, 0, N)

print(cnt_zero)
print(cnt_one)