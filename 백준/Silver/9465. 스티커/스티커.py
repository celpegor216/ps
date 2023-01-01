T = int(input())

for t in range(T):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(2)]
    lst.append([0 for _ in range(N)])

    for n in range(1, N):
        lst[0][n] += max(lst[1][n - 1], lst[2][n - 1])
        lst[1][n] += max(lst[0][n - 1], lst[2][n - 1])
        lst[2][n] += max(lst[0][n - 1], lst[1][n - 1], lst[2][n - 1])

    print(max(lst[0][-1], lst[1][-1], lst[2][-1]))