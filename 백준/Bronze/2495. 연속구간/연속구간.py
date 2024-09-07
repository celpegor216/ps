for _ in range(3):
    now = ''
    cnt = 0
    result = 0
    
    S = input()
    for s in S:
        if s == now:
            cnt += 1
        else:
            cnt = 1
            now = s
        result = max(result, cnt)
    
    print(result)