N = int(input())

total = [0] * (N + 1)
new = [0] * (N + 1)
total[1] = 1
new[1] = 1

for i in range(2, N + 1):
    total[i] = total[i - 1] * 2
    new[i] = total[i - 1]

    if i >= 4 and not i % 2:
        total[i] = total[i] - new[i - 3] - new[i - 4]

print(total[-1])