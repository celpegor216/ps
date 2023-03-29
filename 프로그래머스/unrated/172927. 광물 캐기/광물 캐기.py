def solution(picks, minerals):
    length = len(minerals)
    lst = []
    idx = 0
    while idx < length:
        temp = []
        
        for i in range(5):
            if idx >= length:
                break
            if minerals[idx] == 'diamond':
                temp.append(0)
            elif minerals[idx] == 'iron':
                temp.append(1)
            else:
                temp.append(2)
            idx += 1
        
        lst.append(temp)
    
    picks_total = sum(picks)
    answer = 21e8
    def dfs(level, path):
        nonlocal answer
        
        if level == len(lst) or level == picks_total:
            total = 0
            
            for i in range(level):
                for j in range(len(lst[i])):
                    if path[i] <= lst[i][j]:
                        total += 1
                    else:
                        total += 5 ** (path[i] - lst[i][j])
            
            answer = min(answer, total)
            
            return
        
        for i in range(3):
            if picks[i] > 0:
                picks[i] -= 1
                dfs(level + 1, path + [i])
                picks[i] += 1
    
    dfs(0, [])
    
    return answer