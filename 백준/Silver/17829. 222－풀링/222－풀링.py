N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

while N > 1:
    nxt_N = N // 2
    result = [[0] * nxt_N for _ in range(nxt_N)]

    for i in range(0, N, 2):
        for j in range(0, N, 2):
            tmp = []

            for k in range(2):
                for l in range(2):
                    tmp.append(lst[i + k][j + l])
            
            result[i // 2][j // 2] = sorted(tmp)[2]

    lst = result
    N = nxt_N

print(result[0][0])