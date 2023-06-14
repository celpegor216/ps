while 1:
    n = int(input())

    if n == -1:
        break
    
    lst = [1]
    num = 2

    for i in range(2, n):
        if not n % i:
            lst.append(i)
    
    if sum(lst) == n:
        print(f'{n} = {lst[0]}', end='')

        for i in range(1, len(lst)):
            print(f' + {lst[i]}', end='')
        print()
    else:
        print(f'{n} is NOT perfect.')