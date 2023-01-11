def solution(n):
    answer = []
    
    i = 2
    
    while i <= n:
        if not n % i:
            answer.append(i)
            while 1:
                if not n % i:
                    n //= i
                else:
                    break
        else:
            i += 1
    
    return answer