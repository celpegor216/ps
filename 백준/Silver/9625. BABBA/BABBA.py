K = int(input())

result = [1, 0]

for _ in range(K):
    result = [result[1], result[0] + result[1]]

print(*result)