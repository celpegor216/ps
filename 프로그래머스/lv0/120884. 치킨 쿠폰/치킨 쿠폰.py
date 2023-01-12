def solution(chicken):
    answer = 0
    cupon = 0
    
    for i in range(chicken):
        cupon += 1
        if cupon == 10:
            answer += 1
            cupon = 1
    
    if cupon == 10:
        answer += 1
    
    return answer