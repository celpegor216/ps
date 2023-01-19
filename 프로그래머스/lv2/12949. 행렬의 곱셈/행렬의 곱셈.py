#            \ arr2의 세로  
# arr1의 가로

def solution(arr1, arr2):
    N, M, O = len(arr1), len(arr2[0]), len(arr1[0])
    
    answer = [[0] * M for _ in range(N)]
    
    for n in range(N):
        for m in range(M):
            for o in range(O):
                answer[n][m] += arr1[n][o] * arr2[o][m]
    
    return answer