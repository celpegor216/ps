K, M = map(int, input().split())

primes = [0] * (10 ** 5)
primes[0] = 1
primes[1] = 1

for n in range(2, 10 ** 5):
    now = n * 2
    while now < 10 ** 5:
        primes[now] = 1
        now += n

primes = [x for x in range(2, 10 ** 5) if not primes[x]]
length = len(primes)

temp = set()
for i in range(length):
    for j in range(i + 1, length):
        num = primes[i] + primes[j]
        num_length = len(str(num))
        if num_length == K:
            if num_length == len(set(str(num))):
                temp.add(num)
        elif num_length > K:
            break

mults = set()
for i in range(length):
    for j in range(length):
        num = primes[i] * primes[j]
        if len(str(num)) <= K:
            mults.add(num)
        else:
            break

cnt = 0
for item in temp:
    now = item

    while 1:
        if not now % M:
            now //= M
        else:
            break
    
    if now in mults:
        cnt += 1

print(cnt)