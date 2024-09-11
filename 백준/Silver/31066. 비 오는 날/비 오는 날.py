# 해답: https://velog.io/@nahowo/%EB%B0%B1%EC%A4%80-31066-%EB%B9%84-%EC%98%A4%EB%8A%94-%EB%82%A0Python


T = int(input())

for _ in range(T):
    # 학생 수 N, 우산 수 M, 우산 당 최대 인원 K
    N, M, K = map(int, input().split())

    # 갈 수 있는 최대한 많은 사람
    movable = K * M

    if movable == 1 and N > 1:
        print(-1)
        continue

    result = 1
    while 1:
        if movable >= N:
            break
        N -= (movable - 1)
        result += 2

    print(result)