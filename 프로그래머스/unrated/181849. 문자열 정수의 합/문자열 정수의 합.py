def solution(num_str):
    answer = 0
    
    for item in num_str:
        answer += int(item)
    
    return answer