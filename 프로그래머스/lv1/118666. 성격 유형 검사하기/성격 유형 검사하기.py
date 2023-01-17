def solution(survey, choices):
    answer = ''
    
    dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(survey)):
        types = survey[i]
        score = choices[i] - 4
        if score < 0:
            dic[types[0]] += abs(score)
        elif score > 0:
            dic[types[1]] += abs(score)
    
    for type1, type2 in (('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')):
        if dic[type1] < dic[type2]:
            answer += type2
        else:
            answer += type1
            
    return answer