N = int(input())
q = list(enumerate(map(int, input().split())))

result = [0] * N
for n in range(N):
    idx, value = q[0]
    result[n] = idx + 1

    if n == N - 1:
        break

    new_q = q[1:]
    length = len(new_q)

    if value > 0:
        start_idx = (value - 1) % length
    else:
        start_idx = length - (-value - 1) % length - 1
    q = new_q[start_idx:] + new_q[:start_idx]

print(*result)