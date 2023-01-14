def div(num):
    result = [1]
    
    i = 2
    
    while num and i <= num:
        if not num % i:
            result.append(i)
            num //= i
        else:
            i += 1
    
    return result

def solution(n, m):
    lst_n = div(n)
    lst_m = div(m)
    
    max_gys = 1
    min_gbs = 1
    
    if len(lst_n) < len(lst_m):
        lst_n, lst_m = lst_m, lst_n
    
    for item in set(lst_n):
        if item in lst_m:
            max_gys *= item ** min(lst_n.count(item), lst_m.count(item))
    
    min_gbs = n * m // max_gys
    
    return [max_gys, min_gbs]