S = input()
N = len(S)

result = set()

for n in range(N):
    for m in range(n + 1, N + 1):
        result.add(S[n:m])

print(len(result))