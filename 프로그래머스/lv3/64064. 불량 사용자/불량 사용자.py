def solution(user_id, banned_id):
    bucket = []
    
    for b_id in banned_id:
        temp = []
        for u_id in user_id:
            
            if len(b_id) == len(u_id):
                flag = 0
                
                for i in range(len(b_id)):
                    if b_id[i] != '*' and b_id[i] != u_id[i]:
                        flag = 1
                        break
                
                if not flag:
                    temp.append(u_id)
        
        if temp:
            bucket.append(temp)
    
    
    if len(bucket) == len(banned_id):
        possibles = []
        
        def dfs(level, path):
            nonlocal possibles
            
            if level == len(bucket):
                if sorted(path) not in possibles:
                    possibles.append(sorted(path))
                return
            
            for item in bucket[level]:
                if item not in path:
                    dfs(level + 1, path + [item])
        
        dfs(0, [])
    
    return len(possibles)