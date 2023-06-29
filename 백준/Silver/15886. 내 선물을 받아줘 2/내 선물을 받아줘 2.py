N = int(input())
S = input()

result = 0
idx = 0
now = S[0]

while idx < N:
    if S[idx] != now:
        if now == S[0]:
            result += 1
        now = S[idx]
    idx += 1

if not result:
    print(1)
else:
    print(result)