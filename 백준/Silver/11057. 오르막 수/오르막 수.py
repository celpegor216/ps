N = int(input())

before = [1] * 10
now = [1] * 10

for n in range(N - 1):
    before = now[:]
    now = [1] * 10

    for i in range(1, 10):
        now[i] = before[i] + now[i - 1]

print(sum(now) % 10007)