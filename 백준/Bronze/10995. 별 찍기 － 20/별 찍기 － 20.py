N = int(input())

line = '* ' * N

for n in range(N):
    if n % 2:
        print(' ' + line)
    else:
        print(line)