from copy import deepcopy

def solution(key, lock):
    N, M = len(lock), len(key)
    length = N + M - 1
    temp = [[0] * length for _ in range(length)]
    
    for d in range(4):
        for i in range(N):
            for j in range(N):
                for k in range(M):
                    for l in range(M):
                        temp[i + k][j + l] = key[k][l]
                
                for k in range(M):
                    for l in range(M):
                        flag = 0
                        
                        for v in range(N):
                            if not flag:
                                for h in range(N):
                                    if temp[k + v][l + h] + lock[v][h] != 1:
                                        flag = 1
                                        break
                        
                        if not flag:
                            return True
                
                temp = [[0] * length for _ in range(length)]
        
        key_temp = []
        for i in range(M):
            key_temp.append([key[M - x - 1][i] for x in range(M)])
        
        key = deepcopy(key_temp)
                                
    return False