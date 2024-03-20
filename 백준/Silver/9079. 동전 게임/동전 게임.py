from collections import deque

T = int(input())

for t in range(T):
    lst = []

    for _ in range(3):
        lst += input().split()

    start = ''.join(lst)
    
    q = deque()
    q.append((start, 0))
    used = set()
    used.add(start)

    result = -1

    while q:
        now, cnt = q.popleft()

        if 'H' not in now or 'T' not in now:
            result = cnt
            break

        # 세로 뒤집기
        for i in range(3):
            tmp = ''
            for j in range(1, 10):
                if j % 3 == i:
                    tmp += 'H' if now[j - 1] == 'T' else 'T'
                else:
                    tmp += now[j - 1]
            
            if tmp not in used:
                q.append((tmp, cnt + 1))
                used.add(tmp)

        # 가로 뒤집기
        for i in range(1, 4):
            tmp = ''
            for j in range(9):
                if (i - 1) * 3 <= j < i * 3:
                    tmp += 'H' if now[j] == 'T' else 'T'
                else:
                    tmp += now[j]
            
            if tmp not in used:
                q.append((tmp, cnt + 1))
                used.add(tmp)
                        
        # 대각선 뒤집기
        tmp = ''
        for j in range(9):
            if not j % 4:
                tmp += 'H' if now[j] == 'T' else 'T'
            else:
                tmp += now[j]
        
        if tmp not in used:
            q.append((tmp, cnt + 1))
            used.add(tmp)
        
        tmp = ''
        for j in range(9):
            if 0 < j < 8 and not j % 2:
                tmp += 'H' if now[j] == 'T' else 'T'
            else:
                tmp += now[j]
        
        if tmp not in used:
            q.append((tmp, cnt + 1))
            used.add(tmp)
    
    print(result)