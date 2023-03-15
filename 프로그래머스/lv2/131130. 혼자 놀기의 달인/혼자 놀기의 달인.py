def solution(cards):
    length = len(cards)
    
    group = [0] * length
    
    def dfs(start, now):
        if start == now:
            return
        
        group[now - 1] = start
        dfs(start, cards[now - 1])
    
    for i in range(length):
        if not group[i]:
            group[i] = i + 1
            dfs(i + 1, cards[i])
            
    bucket = [0] * (length + 1)
    for item in group:
        bucket[item] += 1
    
    max_v = max(bucket)
    bucket[bucket.index(max_v)] = 0
    max_v2 = max(bucket)
    
    return max_v * max_v2