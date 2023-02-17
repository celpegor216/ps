def solution(numbers):
    answer = []
    
    for number in numbers:
        num = bin(number)[:2] + '0' + bin(number)[2:]
        
        for i in range(len(num) - 1, 1, -1):
            if num[i] == '0':
                if i == len(num) - 1:
                    answer.append(int(num[:-1] + '1', 2))
                else:
                    answer.append(int(num[:i] + '10' + num[i + 2:], 2))
                break
                
    return answer