# 힌트: dp, 비트마스킹
# 해답: https://velog.io/@e_juhee/python-%EB%B0%B1%EC%A4%80-2098-%EC%99%B8%ED%8C%90%EC%9B%90-%EC%88%9C%ED%9A%8C-DP-%EB%B9%84%ED%8A%B8%EB%A7%88%EC%8A%A4%ED%82%B9-lso2bk58

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = {}

# now: 현재 위치
# visited: 비트마스킹을 이용해 방문한 도시 기록
def dfs(now, visited):
    if visited == (1 << N) - 1:
        # 출발 위치로 돌아갈 수 있는 경우
        if lst[now][0]:
            return lst[now][0]
        else:
            return 21e8
    
    if (now, visited) in dp:
        return dp[(now, visited)]

    # 출발 위치를 제외하고 방문 가능 여부 확인
    minv = 21e8
    for n in range(1, N):
        if not lst[now][n] or visited & (1 << n):
            continue
        minv = min(minv, dfs(n, visited | (1 << n)) + lst[now][n])

    dp[(now, visited)] = minv
    return minv

# 최단 경로를 찾으면 순환이기 때문에 어디서 시작해도 같은 결과가 도출됨
# 따라서 출발 위치는 임의로 설정해도 됨
print(dfs(0, 1))