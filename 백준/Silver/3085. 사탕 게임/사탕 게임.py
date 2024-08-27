N = int(input())
lst = [list(input()) for _ in range(N)]

result = 1

def check_vertical(j):
    global result

    cnt = 0
    now = ''
    for y in range(N):
        if lst[y][j] != now:
            now = lst[y][j]
            cnt = 1
        else:
            cnt += 1
            result = max(result, cnt)

def check_horizontal(i):
    global result

    cnt = 0
    now = ''
    for x in range(N):
        if lst[i][x] != now:
            now = lst[i][x]
            cnt = 1
        else:
            cnt += 1
            result = max(result, cnt)

# 가로로 바꾸고 확인
for i in range(N):
    for j in range(N - 1):
        lst[i][j], lst[i][j + 1] = lst[i][j + 1], lst[i][j]
        check_vertical(j)
        check_vertical(j + 1)
        check_horizontal(i)
        lst[i][j], lst[i][j + 1] = lst[i][j + 1], lst[i][j]

# 세로로 바꾸고 확인
for j in range(N):
    for i in range(N - 1):
        lst[i][j], lst[i + 1][j] = lst[i + 1][j], lst[i][j]
        check_vertical(j)
        check_horizontal(i)
        check_horizontal(i + 1)
        lst[i][j], lst[i + 1][j] = lst[i + 1][j], lst[i][j]

print(result)
