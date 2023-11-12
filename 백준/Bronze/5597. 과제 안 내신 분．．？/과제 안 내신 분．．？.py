check = [0] * 31
for n in range(28):
    check[int(input())] = 1

for n in range(1, 31):
    if not check[n]:
        print(n)