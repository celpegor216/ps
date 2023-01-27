def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        nxt = 0
        
        for s in skill_tree:
            if s in skill:
                if skill.index(s) == nxt:
                    nxt += 1
                else:
                    nxt = -1
                    break
        
        if nxt != -1:
            answer += 1
    
    return answer