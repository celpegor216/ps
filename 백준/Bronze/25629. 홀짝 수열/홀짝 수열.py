N = int(input())
lst = list(map(int, input().split()))

odd = even = 0
for item in lst:
    if item % 2:
        odd += 1
    else:
        even += 1

print(1 if odd == even or odd == even + 1 else 0)