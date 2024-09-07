costs = [0] + list(map(int, input().split()))
MAX = 100
time = [0] * (MAX + 1)

for _ in range(3):
    s, e = map(int, input().split())

    for i in range(s, e):
        time[i] += 1

result = 0
for i in range(1, MAX + 1):
    result += costs[time[i]] * time[i]

print(result)