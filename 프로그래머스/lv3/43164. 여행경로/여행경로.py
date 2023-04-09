def solution(tickets):
    length = len(tickets)
    dic = {}
    
    for ticket in tickets:
        if dic.get(ticket[0]):
            dic[ticket[0]].append([ticket[1], 0])
        else:
            dic[ticket[0]] = [[ticket[1], 0]]
    
    answer = []
    
    def dfs(level, now, path):
        nonlocal answer
        
        if level == length:
            if not answer:
                answer = path[:]
            else:
                flag = 0
                
                for i in range(1, length):
                    if answer[i] != path[i]:
                        if answer[i] > path[i]:
                            flag = 1
                        break
                
                if flag:
                    answer = path[:]
            return
        
        if dic.get(now):
            for i in range(len(dic[now])):
                if not dic[now][i][1]:
                    dic[now][i][1] = 1
                    dfs(level + 1, dic[now][i][0], path + [dic[now][i][0]])
                    dic[now][i][1] = 0
    
    dfs(0, 'ICN', ['ICN'])
        
    return answer