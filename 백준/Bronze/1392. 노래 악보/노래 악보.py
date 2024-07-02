N, Q = map(int, input().split())
lst = [-1]

for _ in range(N):
    n = int(input())
    lst.append(lst[-1] + n)

for _ in range(Q):
    time = int(input())

    for i in range(1, N + 1):
        if lst[i - 1] < time <= lst[i]:
            print(i)
            break