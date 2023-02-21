def solution(cards1, cards2, goal):
    answer = 0
    
    while answer < len(goal):
        if cards1 and cards1[0] == goal[answer]:
            cards1.pop(0)
            answer += 1
        elif cards2 and cards2[0] == goal[answer]:
            cards2.pop(0)
            answer += 1
        else:
            break
    
    return 'Yes' if answer == len(goal) else 'No'