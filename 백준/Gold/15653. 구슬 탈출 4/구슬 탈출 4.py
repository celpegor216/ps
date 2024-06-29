from collections import deque

N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]

ry = rx = by = bx = -1

for n in range(N):
    for m in range(M):
        if lst[n][m] == 'R':
            ry = n
            rx = m
            lst[n][m] = '.'
        if lst[n][m] == 'B':
            by = n
            bx = m
            lst[n][m] = '.'

q = deque()
q.append((ry, rx, by, bx, 0))

used = set()
used.add((ry, rx, by, bx))

result = -1
while q:
    ry, rx, by, bx, cnt = q.popleft()

    if lst[by][bx] == 'O':
        continue

    if lst[ry][rx] == 'O':
        result = cnt
        break
    
    # 왼쪽
    if rx < bx:
        nrx = rx
        while lst[ry][nrx - 1] != '#':
            nrx -= 1

            if lst[ry][nrx] == 'O':
                break
        
        nbx = bx
        while lst[by][nbx - 1] != '#':
            nbx -= 1

            if lst[by][nbx] == 'O':
                break
            elif ry == by and nrx == nbx:
                nbx += 1
                break
        
        if (ry, nrx, by, nbx) not in used:
            q.append((ry, nrx, by, nbx, cnt + 1))
            used.add((ry, nrx, by, nbx))
    else:
        nbx = bx
        while lst[by][nbx - 1] != '#':
            nbx -= 1

            if lst[by][nbx] == 'O':
                break

        nrx = rx
        while lst[ry][nrx - 1] != '#':
            nrx -= 1

            if lst[ry][nrx] == 'O':
                break   
            elif ry == by and nrx == nbx:
                nrx += 1
                break    
        
        if (ry, nrx, by, nbx) not in used:
            q.append((ry, nrx, by, nbx, cnt + 1))
            used.add((ry, nrx, by, nbx))

    # 오른쪽
    if rx > bx:
        nrx = rx
        while lst[ry][nrx + 1] != '#':
            nrx += 1

            if lst[ry][nrx] == 'O':
                break
        
        nbx = bx
        while lst[by][nbx + 1] != '#':
            nbx += 1

            if lst[by][nbx] == 'O':
                break
            elif ry == by and nrx == nbx:
                nbx -= 1
                break
        
        if (ry, nrx, by, nbx) not in used:
            q.append((ry, nrx, by, nbx, cnt + 1))
            used.add((ry, nrx, by, nbx))
    else:
        nbx = bx
        while lst[by][nbx + 1] != '#':
            nbx += 1

            if lst[by][nbx] == 'O':
                break

        nrx = rx
        while lst[ry][nrx + 1] != '#':
            nrx += 1   

            if lst[ry][nrx] == 'O':
                break   
            elif ry == by and nrx == nbx:
                nrx -= 1
                break       
        
        if (ry, nrx, by, nbx) not in used:
            q.append((ry, nrx, by, nbx, cnt + 1))
            used.add((ry, nrx, by, nbx))

    # 위
    if ry < by:
        nry = ry
        while lst[nry - 1][rx] != '#':
            nry -= 1

            if lst[nry][rx] == 'O':
                break
        
        nby = by
        while lst[nby - 1][bx] != '#':
            nby -= 1

            if lst[nby][bx] == 'O':
                break
            elif nry == nby and rx == bx:
                nby += 1
                break
        
        if (nry, rx, nby, bx) not in used:
            q.append((nry, rx, nby, bx, cnt + 1))
            used.add((nry, rx, nby, bx))
    else:
        nby = by
        while lst[nby - 1][bx] != '#':
            nby -= 1

            if lst[nby][bx] == 'O':
                break
        
        nry = ry
        while lst[nry - 1][rx] != '#':
            nry -= 1
            
            if lst[nry][rx] == 'O':
                break
            elif nry == nby and rx == bx:
                nry += 1
                break
        
        if (nry, rx, nby, bx) not in used:
            q.append((nry, rx, nby, bx, cnt + 1))
            used.add((nry, rx, nby, bx))

    # 아래
    if ry > by:
        nry = ry
        while lst[nry + 1][rx] != '#':
            nry += 1

            if lst[nry][rx] == 'O':
                break
        
        nby = by
        while lst[nby + 1][bx] != '#':
            nby += 1

            if lst[nby][bx] == 'O':
                break
            elif nry == nby and rx == bx:
                nby -= 1
                break
        
        if (nry, rx, nby, bx) not in used:
            q.append((nry, rx, nby, bx, cnt + 1))
            used.add((nry, rx, nby, bx))
    else:
        nby = by
        while lst[nby + 1][bx] != '#':
            nby += 1

            if lst[nby][bx] == 'O':
                break
        
        nry = ry
        while lst[nry + 1][rx] != '#':
            nry += 1
            
            if lst[nry][rx] == 'O':
                break
            elif nry == nby and rx == bx:
                nry -= 1
                break
        
        if (nry, rx, nby, bx) not in used:
            q.append((nry, rx, nby, bx, cnt + 1))
            used.add((nry, rx, nby, bx))

print(result)