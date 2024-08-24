N = int(input())
lst = list(map(int, input()))

odd = even = 0

for item in lst:
    if item % 2:
        odd += 1
    else:
        even += 1

if odd > even:
    print(1)
elif odd < even:
    print(0)
else:
    print(-1)