def solution(numbers):
    answer = ''
    
    # 내림차순 정렬
    numbers = sorted([str(x) for x in numbers], reverse=True)
    
    for i in range(1, len(numbers)):
        while i > 0:
            if numbers[i - 1] + numbers[i] < numbers[i] + numbers[i - 1]:
                numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
            else:
                break
            i -= 1
            
    answer = str(int(''.join(numbers)))
    
    return answer