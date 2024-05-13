N, M, T = map(int, input().split())
lst = [[]] + [list(map(int, input().split())) for _ in range(N)]

for _ in range(T):
    x, d, k = map(int, input().split())

    for i in range(x, N + 1, x):
        if d:
            lst[i] = lst[i][k:] + lst[i][:k]
        else:
            lst[i] = lst[i][-k:] + lst[i][:M - k]
    
    new_lst = [x[:] for x in lst]

    flag = 0
    cnt = 0
    total = 0

    for n in range(1, N + 1):
        for m in range(M):
            if lst[n][m] != None:
                if n != N and lst[n][m] == lst[n + 1][m]:
                    new_lst[n][m] = new_lst[n + 1][m] = None
                    flag = 1
                if n != 1 and lst[n][m] == lst[n - 1][m]:
                    new_lst[n][m] = new_lst[n - 1][m] = None
                    flag = 1
                if lst[n][m] == lst[n][m - 1]:
                    new_lst[n][m] = new_lst[n][m - 1] = None
                    flag = 1
                if lst[n][m] == lst[n][(m + 1) % M]:
                    new_lst[n][m] = new_lst[n][(m + 1) % M] = None
                    flag = 1
                if new_lst[n][m] != None:
                    cnt += 1
                    total += new_lst[n][m]
    
    if not flag:
        for n in range(1, N + 1):
            for m in range(M):
                if new_lst[n][m] != None:
                    if new_lst[n][m] > total / cnt:
                        new_lst[n][m] -= 1
                    elif new_lst[n][m] < total / cnt:
                        new_lst[n][m] += 1

    lst = new_lst

result = 0
for n in range(1, N + 1):
    for m in range(M):
        if lst[n][m] != None:
            result += lst[n][m]

print(result)