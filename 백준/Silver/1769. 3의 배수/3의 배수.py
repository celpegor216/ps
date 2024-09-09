N = input()

result = 0
while len(N) > 1:
    result += 1
    N = str(sum(map(int, N)))

N = int(N)

print(result)
print('NO' if N % 3 else 'YES')