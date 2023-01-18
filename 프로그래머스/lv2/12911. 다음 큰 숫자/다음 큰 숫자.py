def solution(n):
    cnt_one = bin(n).count('1')
    
    next = n + 1
    while 1:
        if bin(next).count('1') == cnt_one:
            return next
        next += 1
    