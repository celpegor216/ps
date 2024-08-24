x = []
y = []
N = 3

for _ in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()

result = []
if x[0] == x[1]:
    result.append(x[2])
elif x[0] == x[2]:
    result.append(x[1])
else:
    result.append(x[0])

if y[0] == y[1]:
    result.append(y[2])
elif y[0] == y[2]:
    result.append(y[1])
else:
    result.append(y[0])

print(*result)