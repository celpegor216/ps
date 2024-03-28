S = input()
N = len(S)

idx = 0
result = 1

while result and idx < N:
    n = 0

    while S[idx] == 'w':
        n += 1
        idx += 1

        if idx >= N:
            result = 0
            break

    if n == 0:
        result = 0
        break

    for item in 'olf':
        if idx + n > N or S[idx:idx + n] != item * n:
            result = 0
            break
        
        idx += n

print(result)