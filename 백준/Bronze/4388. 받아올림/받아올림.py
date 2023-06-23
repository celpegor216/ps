while 1:
    a, b = map(int, input().split())

    if a == b == 0:
        break
    
    result = 0

    if a > b:
        a, b = b, a

    add = 0

    while b > 0:
        temp = a % 10 + b % 10 + add
        a //= 10
        b //= 10

        add = 0

        if temp > 9:
            result += 1
            add = 1

    print(result)