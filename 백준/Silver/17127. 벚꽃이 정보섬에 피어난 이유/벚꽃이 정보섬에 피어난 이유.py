N = int(input())
lst = list(map(int, input().split()))

result = 0
def dfs(level, start, split_points):
    global result

    # 3개의 나누는 점을 정한 경우
    if level == 3:
        total = 0
        now = 1
        split_points.append(N - 1)
        for i in range(N):
            now *= lst[i]

            # 나누는 위치라면 지금까지의 곱을 total에 더하고
            # 다음 위치부터 새로 곱하기 위해 준비
            if i in split_points:
                total += now
                now = 1

        result = max(result, total)
        return

    for i in range(start, N - 1):
        dfs(level + 1, i + 1, split_points + [i])

dfs(0, 0, [])

print(result)