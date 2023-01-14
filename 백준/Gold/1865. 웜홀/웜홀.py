# 해답: https://backtony.github.io/algorithm/2021-02-13-algorithm-boj-class4-10/

INF = 21e8

T = int(input())

# 벨만 포드 알고리즘 응용 -> 그래프에 음의 싸이클이 존재하는지 판단
def bf(start):
    distance = [INF] * (N + 1)
    distance[start] = 0

    for i in range(N):
        for edge in edges:
            s, e, t = edge

            # 현재 노드(s)에서 다음 노드(e)로 도달 가능 여부는 판단하지 않음
            # => 최단 거리 테이블이 아닌 음의 싸이클 존재 여부 판단하는 테이블
            if distance[e] > distance[s] + t:
                distance[e] = distance[s] + t

                # 처음에 distance[start]를 0으로 지정했기 때문에,
                # N번 돌고 나서도 갱신한다면 음수가 되었다는 의미이므로 음의 싸이클이 존재함
                if i == N - 1:
                    return True
    return False


for t in range(T):
    N, M, W = map(int, input().split())
    edges = []

    for m in range(M):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for w in range(W):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    # 시작 지점에 관계 없이 음의 사이클이 존재하는지 판단 -> 임의의 시작 지점으로 1 지정
    if bf(1):
        print('YES')
    else:
        print('NO')