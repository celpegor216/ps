def solution(n):
    before_two = 0
    before_one = 1
    now = 0
    
    for i in range(2, n + 1):
        now = before_two + before_one
        before_two = before_one
        before_one = now
    
    return now % 1234567