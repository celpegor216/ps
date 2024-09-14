N = int(input())
lst = list(map(int, input().split()))

result = 0

def dfs(level, left, total):
    global result

    if level == N - 2:
        result = max(result, total)
        return
    
    for i in range(1, N - level - 1):
        new_left = [left[j] for j in range(N - level) if j != i]
        new_total = total + left[i - 1] * left[i + 1]
        dfs(level + 1, new_left, new_total)

dfs(0, lst, 0)

print(result)