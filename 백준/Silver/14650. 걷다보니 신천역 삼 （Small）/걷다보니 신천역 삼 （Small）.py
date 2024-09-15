N = int(input())

result = 0
def dfs(level, total):
    global result

    if level == N:
        if not total % 3:
            result += 1
        return
    
    for i in range(3):
        dfs(level + 1, total + i)

for i in range(1, 3):
    dfs(1, i)

print(result)