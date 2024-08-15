N = int(input())

result = 0
for i in range(1, int(N ** 0.5) + 1):
    if i ** 2 <= N:
        result += 1

print(result)