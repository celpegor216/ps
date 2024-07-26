S = input()
N = len(S)

result = 10
for n in range(1, N):
    if S[n] == S[n - 1]:
        result += 5
    else:
        result += 10

print(result)