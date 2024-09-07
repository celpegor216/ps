N = int(input())
for _ in range(N):
    A, B = input().split('-')

    a = 0
    for i in range(3):
        a += 26 ** (2 - i) * (ord(A[i]) - ord('A'))
    
    if abs(a - int(B)) <= 100:
        print('nice')
    else:
        print('not nice')