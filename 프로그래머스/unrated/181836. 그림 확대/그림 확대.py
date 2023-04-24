def solution(picture, k):
    answer = []
    
    for line in picture:
        temp = ''
        
        for item in line:
            temp += item * k
        
        answer += [temp] * k
    
    return answer