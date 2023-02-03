# 해답: https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-10830-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%96%89%EB%A0%AC-%EC%A0%9C%EA%B3%B1-%EA%B3%A8%EB%93%9C4-%EB%B6%84%ED%95%A0-%EC%A0%95%EB%B3%B5

from copy import deepcopy

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def mult(U, V):
    result = [[0] * (N) for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            temp = 0
            for k in range(N):
                temp += U[i][k] * V[k][j]
            result[i][j] = temp % 1000

    return result

def div_con(A, B):
    if B == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A

    temp = div_con(A, B // 2)
    
    # 제곱하려는 횟수가 홀수면
    if B % 2:
        return mult(mult(temp, temp), A)
    else:
        return mult(temp, temp)

result = div_con(A, B)
for line in result:
    print(*line)