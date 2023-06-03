lst = [int(input()) for _ in range(9)]

used = [0] * 9
answer = []

def dfs(level):
    global answer
    if answer:
        return

    if level == 2:
        result = [lst[i] for i in range(9) if not used[i]]

        if sum(result) == 100:
            answer = sorted(result)
        
        return
    
    for i in range(9):
        if not used[i]:
            used[i] = 1
            dfs(level + 1)
            used[i] = 0

dfs(0)

for item in answer:
    print(item)