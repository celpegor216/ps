N = int(input())
lst = [input() for _ in range(N)]

result = 0

for i in range(N):
    cnt = set()

    for j in range(N):
        if lst[i][j] == 'Y':
            cnt.add(j)
            
            for k in range(N):
                if lst[j][k] == 'Y':
                    cnt.add(k)
    
    if i in cnt:
        cnt.remove(i)

    result = max(result, len(cnt))

print(result)