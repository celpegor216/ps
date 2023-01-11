       
def solution(spell, dic):    
    for word in dic:
        spell_cnt = [0] * len(spell)
        
        for s in word:
            if s in spell:
                spell_cnt[spell.index(s)] += 1
        
        flag = 0
        
        for i in range(len(spell)):
            if spell_cnt[i] != 1:
                flag = 1
                break
        
        if not flag:
            return 1
    
    return 2