N = int(input())

result = 0

for i in range(1, N + 1):
    half = int(i ** 0.5) + 1
    cnt = 1

    for j in range(2, half):
        if not i % j:
            cnt += 1

    result += cnt

print(result)