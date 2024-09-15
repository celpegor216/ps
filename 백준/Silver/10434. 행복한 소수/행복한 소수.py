TC = int(input())

for tc in range(1, TC + 1):
    _, N = map(int, input().split())

    result = 'NO'

    if N == 1:
        print(tc, N, result)
        continue
    
    # 소수 판정
    half = int(N ** 0.5) + 1
    flag = 0
    for i in range(2, half):
        if not N % i:
            flag = 1
            break
    
    if flag:
        print(tc, N, result)
        continue

    # 행복한 수 판정
    now = N
    used = set()
    used.add(now)
    while 1:
        nxt = 0
        while now:
            nxt += (now % 10) ** 2
            now //= 10
        
        if nxt == 1:
            result = 'YES'
            break
        
        if nxt in used:
            break
        
        used.add(nxt)
        now = nxt

    print(tc, N, result)