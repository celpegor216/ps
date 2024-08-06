lst = list(map(int, input().split()))
N = 10

result = 0
def dfs(level, total, now):
    global result

    # 남은 문제를 다 맞춰도 5개 미만이라면 종료
    if total + N - level < 5:
        return

    if level == N:
        result += 1
        return

    for i in range(1, 6):
        if level > 1 and now[-1] == now[-2] == i:
            continue
        dfs(level + 1, total + 1 if lst[level] == i else total, now + [i])

dfs(0, 0, [])

print(result)