# 힌트: 문자열, 브루트포스, 재귀
# 힌트2: t에서 제거하는 방법으로 구현

S = input()
T = input()
length = len(S)
result = 0
used = []

def dfs(now):
    global result

    if result or len(now) < length:
        return
    
    if now == S:
        result = 1
        return
    
    if now[-1] == 'A':
        temp = now[:-1]
        if not result and temp not in used:
            used.append(temp)
            dfs(temp)
    
    if now[0] == 'B':
        temp = now[len(now) - 1:0:-1]
        if not result and temp not in used:
            used.append(temp)
            dfs(temp)

dfs(T)

print(result)