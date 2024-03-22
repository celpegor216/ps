def solution(n, tops):
    mod = 10007
    
    include_end = exclude_end = 0
    
    if tops[0]:
        include_end = 4
        exclude_end = 3
    else:
        include_end = 3
        exclude_end = 2
    
    for i in range(1, n):
        if tops[i]:
            next_include_end = include_end * 3 + exclude_end
            next_exclude_end = include_end * 2 + exclude_end
        else:
            next_include_end = include_end * 2 + exclude_end
            next_exclude_end = include_end * 1 + exclude_end
        include_end = next_include_end % mod
        exclude_end = next_exclude_end % mod
            
    return include_end % mod