from math import ceil

N = int(input())
lst = list(map(int, input().split()))
B, C = map(int, input().split())

total = N

for n in lst:
    if n > B:
        total += ceil((n - B) / C)

print(total)