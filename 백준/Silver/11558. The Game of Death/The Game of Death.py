T = int(input())

for _ in range(T):
    N = int(input())
    lst = [int(input()) - 1 for _ in range(N)]

    used = [0] * N
    now = 0    # 현재 플레이어
    cnt = 0    # 지목한 횟수
    result = 0
    while 1:
        # 현재 플레이어는 방문 처리
        used[now] = 1

        # 다음 사람 지목
        cnt += 1
        now = lst[now]

        # 이미 지목한 사람이라면 사이클이 생긴 것
        # 목적지에 영원히 도달할 수 없으므로 그냥 종료
        if used[now]:
            break

        # 목적지에 도달한 경우 정답 갱신하고 종료
        if now == N - 1:
            result = cnt
            break

    print(result)