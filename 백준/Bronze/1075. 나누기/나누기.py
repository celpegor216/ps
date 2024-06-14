N = int(input())
F = int(input())

for n in range(100):
    if not (N - N % 100 + n) % F:
        print(n if n > 9 else '0' + str(n))
        break