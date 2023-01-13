def solution(quiz):
    answer = []
    
    for line in quiz:
        x, calc, y, equal, z = line.split()
        
        if calc == '+':
            if int(x) + int(y) == int(z):
                answer.append('O')
            else:
                answer.append('X')
        else:
            if int(x) - int(y) == int(z):
                answer.append('O')
            else:
                answer.append('X')
    
    return answer