def solution(players, callings):
    length = len(players)
    dic = {}
    
    for i in range(length):
        dic[players[i]] = i
    
    for calling in callings:
        idx = dic[calling]
        
        players[idx], players[idx - 1] = players[idx - 1], players[idx]
        
        dic[calling] -= 1
        dic[players[idx]] += 1
    
    return players