S = int(input())

if S in (1, 2):
    print(1)
else:
    now = 2
    total = 3

    while 1:
        if total <= S < total + now + 1:
            print(now)
            break
        else:
            now += 1
            total += now