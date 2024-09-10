S = input()
N = len(S)

result = 'z' * N
for i in range(1, N - 1):
    for j in range(i + 1, N):
        tmp = S[:i][::-1] + S[i:j][::-1] + S[j:][::-1]
        result = min(result, tmp)

print(result)