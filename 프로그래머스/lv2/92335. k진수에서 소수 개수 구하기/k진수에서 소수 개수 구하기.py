# 1, 11, 12 런타임 에러 해결: https://yeoooo.github.io/algorithm/P_92335/

def solution(n, k):
    answer = 0
    
    s = ''
    while n:
        s += str(n % k)
        n //= k
    
    s = s[::-1]
    
    lst = s.split('0')
        
    for item in lst:
        if item != '':
            item = int(item)
            if item != 1:
                flag = 0

                for i in range(2, int(item ** 0.5) + 1):
                    if not item % i:
                        flag = 1
                        break

                if not flag:
                    answer += 1
    
    return answer