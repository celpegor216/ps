n = int(input())

primes = [0] * (n + 1)
primes[0] = 1
primes[1] = 1

for i in range(2, n + 1):
    now = i * 2
    
    while now <= n:
        primes[now] = 1
        now += i

primes = [x for x in range(2, n + 1) if not primes[x]]

for prime in primes:
    temp = [prime]
    now = prime
    flag = 0

    while 1:
        total = 0
        for n in str(now):
            total += int(n) ** 2
        
        if total == 1:
            flag = 1
            break
        
        if total in temp:
            break

        temp.append(total)
        now = total
    
    if flag:
        print(prime)