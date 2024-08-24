N = int(input())
lst = list(map(int, input().split()))

Y = M = 0
for item in lst:
    item += 1
    Y += (item // 30) * 10 + (10 if item % 30 else 0)
    M += (item // 60) * 15 + (15 if item % 60 else 0)

if Y < M:
    print('Y', Y)
elif Y > M:
    print('M', M)
else:
    print('Y M', Y)