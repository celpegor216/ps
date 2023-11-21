T = int(input())

for t in range(T):
    a, b = input().split()

    # a의 길이가 더 길도록
    if len(a) < len(b):
        a, b = b, a

    a = a[::-1]
    b = b[::-1]

    result = [0] * (len(a) + 1)

    for i in range(len(a)):
        if i < len(b):
            if a[i] == b[i] == '1':
                result[i] = 2
            elif not (a[i] == b[i] == '0'):
                result[i] = 1
        else:
            if a[i] == '1':
                result[i] = 1
    
    for i in range(len(a)):
        if result[i] > 1:
            result[i] -= 2
            result[i + 1] += 1
    
    result = result[::-1]
    
    start = 0

    while start < len(result):
        if result[start] == 0:
            start += 1
        else:
            break
    
    result = result[start:]

    if not result:
        result = [0]

    for item in result:
        print(item, end='')

    print()