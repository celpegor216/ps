N, K = map(int, input().split())
lst = list(map(int, input().split(',')))

for _ in range(K):
    tmp = []
    for n in range(1, N):
        tmp.append(lst[n] - lst[n - 1])
    N -= 1
    lst = tmp

print(*lst, sep=',')