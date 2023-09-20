N = int(input())

if N % 2:
    print('1 2 ' * (N // 2), end='')
    print(3)
else:
    print('1 2 ' * (N // 2))