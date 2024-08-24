N = int(input())
lst = [input() for _ in range(N)]

D = P = 0

for n in range(N):
    if lst[n] == 'D':
        D += 1
    else:
        P += 1
    
    if abs(D - P) == 2:
        break

print(f'{D}:{P}')