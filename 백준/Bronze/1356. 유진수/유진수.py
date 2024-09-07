S = input()
N = len(S)

for n in range(1, N):
    A = S[:n]
    B = S[n:]
    
    a = b = 1
    for i in A:
        a *= int(i)
    for i in B:
        b *= int(i)
    
    if a == b:
        print('YES')
        break
else:
    print('NO')