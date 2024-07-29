T = int(input())

N = 6
for _ in range(T):
    M = int(input())
    lst = list(map(int, input().split()))

    result = 0

    while 1:
        result += 1

        if sum(lst) > M:
            break

        new_lst = [0] * N
        for i in range(N):
            new_lst[i] = lst[i] + lst[i - 1] + lst[(i + 1) % N] + lst[(i + N // 2) % N]
        lst = new_lst

    print(result)