# 플로이드 워셜 같은데 구현 방법이 잘 기억 안 나서 풀이 참고

def solution(n, s, a, b, fares):
    answer = [[21e8] * (n + 1) for _ in range(n + 1)]
    
    for fare in fares:
        A, B, C = fare
        answer[A][B] = C
        answer[B][A] = C
    
    for k in range(n + 1): # via
        for i in range(n + 1): # start
            for j in range(n + 1): # end
                if answer[i][j] > answer[i][k] + answer[k][j]:
                    answer[i][j] = answer[i][k] + answer[k][j]
    
    for i in range(n + 1):
        answer[i][i] = 0
    
    # 합승하지 않은 경우
    min_v = answer[s][a] + answer[s][b]
    
    # 합승하는 경우, 어디에서 합승할 건지
    for i in range(n + 1):
        if min_v > answer[s][i] + answer[i][a] + answer[i][b]:
            min_v = answer[s][i] + answer[i][a] + answer[i][b]
    
    return min_v