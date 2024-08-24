N = 3
buttons = [5 * 60, 60, 10]

T = int(input())

result = [0] * N
for i in range(N):
    result[i] += T // buttons[i]
    T %= buttons[i]

if T:
    print(-1)
else:
    print(*result)