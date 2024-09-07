N, M = map(int, input().split())

result = [0] * M

for _ in range(N):
    S = input()
    for m in range(M):
        if S[m] == 'O':
            result[m] = 1

for m in range(M):
    if not result[m]:
        print(m + 1)
        break
else:
    print('ESCAPE FAILED')