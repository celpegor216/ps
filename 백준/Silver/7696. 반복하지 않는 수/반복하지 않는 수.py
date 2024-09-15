MAX = 10 ** 6

numbers = '0123456789'
q = list(numbers[1:])

idx = 0
while len(q) < MAX:
    now = q[idx]

    for n in numbers:
        if n in now:
            continue

        q.append(now + n)
    
    idx += 1

while 1:
    N = int(input())
    
    if N == 0:
        break
    
    N -= 1
    print(q[N])