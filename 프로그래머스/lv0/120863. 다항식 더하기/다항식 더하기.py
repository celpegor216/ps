def solution(polynomial):
    answer = ''
    
    x = 0
    num = 0
    
    lst = polynomial.split()
    for item in lst:
        if item[-1] == 'x':
            if len(item) > 1:
                x += int(item[:-1])
            else:
                x += 1
        elif item != '+':
            num += int(item)
            
    if x > 1:
        answer += f'{x}x'
    elif x == 1:
        answer += 'x'
    
    if num > 0:
        if answer:
            answer += f' + {num}'
        else:
            answer += str(num)
    
    if not answer:
        answer = '0'
        
    return answer