def solution(numer1, denom1, numer2, denom2):
    numer, denom = numer1 * denom2 + numer2 * denom1, denom1 * denom2
    
    for i in range(2, numer + 1):
        while 1:
            if not numer % i and not denom % i:
                numer //= i
                denom //= i
            else:
                break
    
    return [numer, denom]