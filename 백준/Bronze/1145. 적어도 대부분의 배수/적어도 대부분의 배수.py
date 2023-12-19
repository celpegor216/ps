lst = list(map(int, input().split()))

result = 1

while 1:
    flag = 0

    for item in lst:
        if not result % item:
            flag += 1
    
    if flag > 2:
        print(result)
        break

    result += 1