from collections import deque

N, K = map(int, input().split())

minc = 21e8
cnt = 0

q = deque()
q.append((N, 0))

used = [0] * 100001
used[N] = 0

if N == K:
    minc = 0
    cnt = 1
else:
    t = 0
    temp = set()
    
    while q:
        nown, nowc = q.popleft()
        
        if nowc > t:
            for item in temp:
                used[item] = 1
            temp = set()
            t = nowc
        
        if nowc > minc:
            break
        
        if nown == K:
            if nowc < minc:
                minc = nowc
                cnt = 1
            elif nowc == minc:
                cnt += 1
            continue
        
        plus1 = nown + 1
        minus1 = nown - 1
        mult2 = nown * 2
        
        if 0 <= plus1 <= 100000 and not used[plus1]:
            q.append((plus1, nowc + 1))
            temp.add(plus1)
        if 0 <= minus1 <= 100000 and not used[minus1]:
            q.append((minus1, nowc + 1))
            temp.add(minus1)
        if 0 <= mult2 <= 100000 and not used[mult2]:
            q.append((mult2, nowc + 1))
            temp.add(mult2)
        
print(minc)
print(cnt)