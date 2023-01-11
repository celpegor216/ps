# 0:n , n:n*2, n*2:n*3 ...

def solution(num_list, n):
    answer = []
    
    for i in range(len(num_list) // n):
        answer.append(num_list[n * i:n * (i + 1)])
    
    return answer