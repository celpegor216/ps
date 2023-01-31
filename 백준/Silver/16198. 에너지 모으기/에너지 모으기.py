N = int(input())
lst = list(map(int, input().split()))

result = 0

def dfs(total, lst):
    global result

    if len(lst) < 3:
        result = max(result, total)
        return

    for i in range(1, len(lst) - 1):
        dfs(total + lst[i - 1] * lst[i + 1], lst[:i] + lst[i + 1:])

dfs(0, lst)

print(result)