def dfs(level, path):
    global bab, lst, used
    
    if level == 5:
        return
    
    lst.append(path)
    
    for i in range(4):
        if not used[i]:
            used[i] = 1
            dfs(level + 1, path + bab[i])
            used[i] = 0
            
bab = ["aya", "ye", "woo", "ma"]
lst = []
used = []

def solution(babbling):
    global lst, used
    used = [0] * 4
    
    dfs(0, '')
    
    answer = 0
    
    for item in babbling:
        if item in lst:
            answer += 1
    
    return answer