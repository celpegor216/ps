N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

# distances[i][j]: i번 집에서 j번 집까지 거리
distances = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        dist = abs(lst[i][0] - lst[j][0]) + abs(lst[i][1] - lst[j][1])
        distances[i][j] = dist
        distances[j][i] = dist

result = 21e8
def dfs(level, start, selected_houses):
    global result

    # 대피소로 삼을 집 K개 선정이 완료되었을 때
    if level == K:
        maxv = 0
        
        for i in range(N):
            # 각 집에서 대피소로 선정한 집들 중 가장 가까운 거리를 탐색
            minv = 21e8
            if i in selected_houses:
                continue

            for j in selected_houses:
                minv = min(minv, distances[i][j])
    
            # 가장 가까운 거리의 최댓값을 maxv에 저장
            maxv = max(maxv, minv)
        
        # 가장 가까운 거리의 최댓값과 result를 비교해서 더 작은 값을 result에 저장
        result = min(result, maxv)
        return

    # 순열이 아닌 조합이므로 used 배열 없이 이전에 고른 것 다음 것부터 고르면 됨
    for i in range(start, N):
        dfs(level + 1, i + 1, selected_houses + [i])

dfs(0, 0, [])

print(result)