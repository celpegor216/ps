T = int(input())

# 시계 방향으로 45도 회전
def rotate():
    global lst

    new_lst = [line[:] for line in lst]

    # X의 주 대각선을 ((1,1), (2,2), …, (n, n)) 가운데 열 ((n+1)/2 번째 열)로 옮긴다.
    for i in range(N):
        new_lst[i][N // 2] = lst[i][i]

    # X의 가운데 열을 X의 부 대각선으로 ((n, 1), (n-1, 2), …, (1, n)) 옮긴다. 
    for i in range(N):
        new_lst[i][N - i - 1] = lst[i][N // 2]

    # X의 부 대각선을 X의 가운데 행 ((n+1)/2번째 행)으로 옮긴다.
    for i in range(N):
        new_lst[N // 2][N - i - 1] = lst[i][N - i - 1]

    # X의 가운데 행을 X의 주 대각선으로 옮긴다.
    for i in range(N):
        new_lst[i][i] = lst[N // 2][i]

    # 위 네 가지 경우 모두 원소의 기존 순서는 유지 되어야 한다.
    # X의 다른 원소의 위치는 변하지 않는다.

    lst = new_lst
    

for _ in range(T):
    N, D = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    if D != 0:
        if D > 0:
            for _ in range(D // 45):
                rotate()
        else:
            for _ in range((360 + D) // 45):
                rotate()
    
    for line in lst:
        print(*line)
