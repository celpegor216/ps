X = int(input())
N = int(input())

total = 0
for n in range(N):
    cost, num = map(int, input().split())
    total += cost * num

if total == X:
    print('Yes')
else:
    print('No')