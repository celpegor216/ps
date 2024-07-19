lst = []

for _ in range(10):
    num = int(input())

    if not lst:
        lst.append(num)
    else:
        lst.append(lst[-1] + num)

result = 0

for item in lst:
    if abs(100 - item) < abs(100 - result) or (abs(100 - item) == abs(100 - result) and item > result):
        result = item

print(result)