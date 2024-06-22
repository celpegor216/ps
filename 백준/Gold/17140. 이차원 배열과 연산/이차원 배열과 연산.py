R, C, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(3)]

R -= 1
C -= 1

N = M = 3
result = 0

while result < 101:
    if N > R and M > C and lst[R][C] == K:
        break

    if N >= M:
        tmp_lst = []
        new_M = 0

        for n in range(N):
            dic = dict()

            for m in range(M):
                dic[lst[n][m]] = dic.get(lst[n][m], 0) + 1
            
            tmp = []
            for k, v in sorted(dic.items(), key=lambda x: (x[1], x[0])):
                if k == 0:
                    continue
                tmp.append(k)
                tmp.append(v)

            new_M = max(new_M, len(tmp))
            tmp_lst.append(tmp)
        
        new_M = min(new_M, 100)

        new_lst = [[0] * new_M for _ in range(N)]
        
        for n in range(N):
            for m in range(len(tmp_lst[n])):
                new_lst[n][m] = tmp_lst[n][m]

        lst = new_lst
        M = new_M
    else:
        tmp_lst = []
        new_N = 0

        for m in range(M):
            dic = dict()

            for n in range(N):
                dic[lst[n][m]] = dic.get(lst[n][m], 0) + 1
            
            tmp = []
            for k, v in sorted(dic.items(), key=lambda x: (x[1], x[0])):
                if k == 0:
                    continue
                tmp.append(k)
                tmp.append(v)

            new_N = max(new_N, len(tmp))
            tmp_lst.append(tmp)
        
        new_N = min(new_N, 100)

        new_lst = [[0] * M for _ in range(new_N)]
        
        for m in range(M):
            for n in range(len(tmp_lst[m])):
                new_lst[n][m] = tmp_lst[m][n]

        lst = new_lst
        N = new_N
    
    result += 1

print(result if result < 101 else -1)