def solution(num, k):
    num, k = str(num), str(k)
    
    if k in num:
        return num.index(k) + 1
    else:
        return -1
