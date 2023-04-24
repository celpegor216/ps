def solution(num_list):
    answer = 0
    
    for item in num_list:
        while item > 1:
            if item % 2:
                item -= 1
            item //= 2
            answer += 1
    
    return answer