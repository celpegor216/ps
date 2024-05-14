A, B = map(int, input().split())

half = int(B ** 0.5) + 1
check = [0] * half
primes = []

for i in range(2, half):
    if not check[i]:
        primes.append(i)
        j = i * 2
        while j < half:
            check[j] = 1
            j += i

result = 0
for prime in primes:
    p = prime ** 2
    while p <= B:
        if p >= A:
            result += 1
        p *= prime

print(result)