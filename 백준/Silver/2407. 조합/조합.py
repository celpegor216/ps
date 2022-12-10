# nCm = n! / (n-m)!m!

n, m = map(int, input().split())

numerator = [x for x in range(1, n + 1)]

denominator = [x for x in range(1, n - m + 1)] + [y for y in range(1, m + 1)]

nu = 1
for num in numerator:
    nu *= num

de = 1
for num in denominator:
    de *= num

print(nu // de)