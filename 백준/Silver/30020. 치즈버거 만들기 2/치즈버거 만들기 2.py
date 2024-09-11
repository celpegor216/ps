A, B = map(int, input().split())

if A <= B or A > B * 2:
    print('NO')
else:
    print('YES')
    print(A - B)
    for i in range(A - B - 1):
        print('aba')
    print('a' + 'ba' * (B + 1 - (A - B)))