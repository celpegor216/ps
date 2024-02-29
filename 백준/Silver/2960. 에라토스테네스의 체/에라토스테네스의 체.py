N, K = map(int, input().split())
primes = [0] * (N + 1)
primes[0] = 1
primes[1] = 1

result = -1

for p in range(2, N + 1):
    if not primes[p]:
        i = p

        while i <= N:
            if not primes[i]:
                primes[i] = 1
                K -= 1

            if not K:
                result = i
                break

            i += p
        
        if result != -1:
            print(result)
            break