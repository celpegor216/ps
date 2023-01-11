def solution(emergency):
    answer = []
    
    sorted_emergency = sorted(emergency, reverse=True)
    
    for item in emergency:
        answer.append(sorted_emergency.index(item) + 1)
    
    return answer