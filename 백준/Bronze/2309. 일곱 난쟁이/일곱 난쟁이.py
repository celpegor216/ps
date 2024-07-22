lst = [int(input()) for _ in range(9)]

result = []
total = sum(lst)

for i in range(8):
    if result:
        break

    for j in range(i + 1, 9):
        if lst[i] + lst[j] == total - 100:
            result = [i, j]
            break

result = sorted([lst[n] for n in range(9) if n not in result])

for item in result:
    print(item)