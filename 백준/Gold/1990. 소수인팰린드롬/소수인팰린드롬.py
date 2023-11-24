a, b = input().split()

a = list(map(int, a))
b = int(b)

length = len(a)
halflength = len(a) // 2 if not len(a) % 2 else (len(a) // 2) + 1
half = a[:halflength]

while 1:
    num = ''

    for item in half:
        num += str(item)

    if length % 2:
        num += num[:-1][::-1]
    else:
        num += num[::-1]
    
    num = int(num)

    if num > b:
        break

    root = int(num ** 0.5) + 1

    flag = 0

    for i in range(2, root):
        if not num % i:
            flag =1
            break
    
    if not flag:
        print(num)


    half[-1] += 1

    for i in range(halflength - 1, -1, -1):
        if half[i] == 10:
            if i != 0:
                half[i] = 0
                half[i - 1] += 1
            else:
                if not length % 2:
                    halflength += 1
                length += 1
                
                half = [1] + [0] * (halflength - 1)

print(-1)