def solution(str_list, ex):
    answer = ''
    
    for item in str_list:
        if ex not in item:
            answer += item
    
    return answer