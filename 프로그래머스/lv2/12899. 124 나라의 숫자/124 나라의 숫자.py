def solution(n):
    answer = []
    
    while n:
        answer.append(n % 3)
        n //= 3
        
    idx = 0
    while idx < len(answer):
        if answer[idx] < 1 and idx + 1 < len(answer):
            answer[idx] += 3
            answer[idx + 1] -= 1
        idx += 1
    
    return ''.join(map(str, answer))[::-1].replace('0', '').replace('3', '4')