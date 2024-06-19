N = int(input())
S = input()

result = ''
def dfs(level, now):
    global result

    if result:
        return

    if level == N:
        flag = 0
        stack = []

        for n in range(N):
            if now[n] == '(':
                stack.append(1)
            else:
                stack.pop()
        if stack:
            flag = 1

        if not flag:
            result = ''.join(now)
        return
    
    if now[level] == 'G':
        now[level] = '('
        dfs(level + 1, now)
        now[level] = ')'
        dfs(level + 1, now)
    else:
        dfs(level + 1, now)

dfs(0, list(S))

print(result)