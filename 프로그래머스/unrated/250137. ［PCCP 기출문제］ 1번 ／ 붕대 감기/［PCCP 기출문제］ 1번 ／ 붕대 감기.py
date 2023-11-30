def solution(bandage, health, attacks):
    now = health
    time = 0
    
    for attack in attacks:
        tmp = attack[0] - time
        cnt = tmp // bandage[0]
        
        now += tmp * bandage[1] + cnt * bandage[2]
        
        if now > health:
            now = health
        
        now -= attack[1]
        
        if now <= 0:
            return -1
        
        time = attack[0] + 1
    
    return now