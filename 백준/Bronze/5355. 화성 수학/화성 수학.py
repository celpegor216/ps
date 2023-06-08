T = int(input())

for t in range(T):
    lst = input().split()
    num = float(lst[0])

    for i in range(1, len(lst)):
        if lst[i] == '@':
            num *= 3
        elif lst[i] == '%':
            num += 5
        else:
            num -= 7
    
    print('%.2f' % num)