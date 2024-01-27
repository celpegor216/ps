lst = [0] * 10001

def check(i):

    total = i

    tmp = i

    

    while tmp:

        total += tmp % 10

        tmp //= 10

    if total > 10000:

        return

    

    if not lst[total]:

        lst[total] = 1

        check(total)

for i in range(1, 10001):

    if not lst[i]:

        check(i)

for i in range(1, 10001):

    if not lst[i]:

        print(i)