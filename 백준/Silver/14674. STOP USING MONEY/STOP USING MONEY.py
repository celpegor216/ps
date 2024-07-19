# 해답: https://risk-boy.github.io/boj/14674/

N, K = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        a, b = lst[i][1] * lst[j][2], lst[i][2] * lst[j][1]

        if a > b:
            lst[i], lst[j] = lst[j], lst[i]
        elif a == b:
            if lst[i][1] > lst[j][1]:
                lst[i], lst[j] = lst[j], lst[i]
            elif lst[i][1] == lst[j][1]:
                if lst[i][0] > lst[j][0]:
                    lst[i], lst[j] = lst[j], lst[i]

for i, c, h in lst[:K]:
    print(i)