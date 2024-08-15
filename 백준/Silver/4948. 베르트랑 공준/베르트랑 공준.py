N = 123456

primes = [1] * (N * 2)

for i in range(2, N + 1):
    if not primes[i]:
        continue
    j = i * 2
    while j < N * 2:
        primes[j] = 0
        j += i

while 1:
    num = int(input())

    if not num:
        break

    print(sum(primes[num + 1:num * 2 + 1]))