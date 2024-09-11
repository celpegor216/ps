T = int(input())

for _ in range(T):
    W, N = map(int, input().split())
    # 거리, 무게
    lst = [list(map(int, input().split())) for _ in range(N)]

    # 쓰레기 모으기는 쓰레기차가 모든 지점의 쓰레기를 수거하여 쓰레기장에 도달했을 때 끝난다.
    result = lst[-1][0]
    now_weight = 0
    # 쓰레기차는 쓰레기장에서 가까운 지점부터 방문하며,
    for n in range(N):
        # 쓰레기를 모으다가 다음과 같은 경우에 쓰레기장으로 돌아가 싣고 있는 쓰레기를 비운다.
            # 쓰레기의 양이 용량에 도달했을 때.
            # 그 지점의 쓰레기를 실었을 때 쓰레기차의 용량을 넘게 될 때.
            # 더 이상 쓰레기를 실을 지점이 없을 때.
        # 쓰레기차가 특정 지점에서 쓰레기를 실을 때는 한 번에 모두 실어야 한다.
        # (즉, 쓰레기의 일부를 싣고 쓰레기장에 다녀온 뒤 나머지를 싣는 것은 허용되지 않는다.)
        if now_weight + lst[n][1] > W:
            result += lst[n][0] * 2
            now_weight = 0

        now_weight += lst[n][1]

        if now_weight == W:
            if n == N - 1:
                result += lst[n][0]
            else:
                result += lst[n][0] * 2
            now_weight = 0

    if now_weight != 0:
        result += lst[-1][0]

    print(result)