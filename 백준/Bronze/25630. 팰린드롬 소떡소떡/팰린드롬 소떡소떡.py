N = int(input())
S = input()

result = 0
for n in range(N // 2):
    if S[n] != S[N - 1 - n]:
        result += 1

print(result)