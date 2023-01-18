def solution(n,a,b):
    answer = 0
    
    while 1:
        answer += 1
        if (not a % 2 and b == a - 1) or (not b % 2 and a == b - 1):
            break
        else:
            a = a // 2 if not a % 2 else (a + 1) // 2
            b = b // 2 if not b % 2 else (b + 1) // 2
    
    return answer