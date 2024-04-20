N, D = input().split()

result = 0

for n in range(1, int(N) + 1):
    result += str(n).count(D)

print(result)