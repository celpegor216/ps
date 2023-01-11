def solution(my_str, n):
    answer = []
    
    length = len(my_str) // n if not len(my_str) % n else len(my_str) // n + 1 
    
    for i in range(length):
        answer.append(my_str[n * i:n * (i + 1)])
    
    return answer