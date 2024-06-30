while 1:
    S = input()
    
    if S == '#':
        break
        
    S = S.lower()
    
    used = [0] * 26
    for s in S:
        if 'a' <= s <= 'z':
            used[ord(s) - ord('a')] = 1
            
    print(sum(used))