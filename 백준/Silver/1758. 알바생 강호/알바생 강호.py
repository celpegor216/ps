import sys
input = sys.stdin.readline

N = int(input())

lst = []

for n in range(N):
    lst.append(int(input()))

total = 0

lst.sort(reverse=True)

for n in range(N):
    tip = lst[n] - n
    if tip > 0:
        total += tip

print(total)