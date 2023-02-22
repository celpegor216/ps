def solution(expression):            
    answer = 0
    
    # 연산자
    calcs = '+-*'
    
    # 연산자 우선순위 경우의 수
    orders = ['+-*', '+*-', '-+*', '-*+', '*+-', '*-+']
    
    # 연산자와 피연산자 분리
    lst = []
    idx = 0
    for i in range(len(expression)):
        if expression[i] in calcs:
            lst.append(int(expression[idx:i]))
            lst.append(expression[i])
            idx = i + 1
    lst.append(int(expression[idx:]))
    
    for order in orders:
        temp = lst[:]
        
        for calc in order:
            idx = 0
            while idx < len(temp):
                if temp[idx] == calc:
                    num = temp.pop(idx - 1)
                    temp.pop(idx - 1)
                    
                    if calc == '+':
                        temp[idx - 1] += num
                    elif calc == '-':
                        temp[idx - 1] = num - temp[idx - 1]
                    else:
                        temp[idx - 1] *= num
                else:
                    idx += 1
        
        if abs(temp[0]) > answer:
            answer = abs(temp[0])
    
    return answer