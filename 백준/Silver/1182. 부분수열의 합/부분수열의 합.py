N, S = map(int, input().split())
lst = list(map(int, input().split()))

result = 0

def dfs(level, start, now):
    global result

    # 크기가 양수인 부분수열의 원소를 다 더한 값이 S인 경우의 수
    if level and now == S:
         result += 1

    if level == N:
        return

    for i in range(start, N):
        dfs(level + 1, i + 1, now + lst[i])

dfs(0, 0, 0)

print(result)