import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = []

for _ in range(N):
    name, power = input().split()
    lst.append((name, int(power)))

powers = [[int(input()), m] for m in range(M)]
powers.sort()
result = [''] * M

idx = 0
for power, m in powers:
    while idx < N and power > lst[idx][1]:
        idx += 1
    result[m] = idx

for m in result:
    print(lst[m][0])