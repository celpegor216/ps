# n = 1  1
# n = 2  1+1, 2
# n = 3  1+1+1, 2+1, 1+2
# n = 4  1+1+1+1, 2+1+1, 1+2+1, 1+1+2, 2+2
# n = k  (n = k - 1) + (n = k - 2)


def solution(n):
    answer = 0
    
    if n == 1:
        return 1
    else:
        before_two = 1
        before_one = 1
        now = 0
        
        for i in range(2, n + 1):
            now = before_two + before_one
            before_two = before_one
            before_one = now
            
        return now % 1234567