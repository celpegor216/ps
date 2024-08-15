N = int(input())

a = 1    # 분자
b = 1    # 분모

total = 2
direction = -1
for _ in range(N - 1):
    if a == 1:
        if a + b == total:
            b += 1
            continue
        else:
            total += 1
            direction *= -1
    elif b == 1:
        if a + b == total:
            a += 1
            continue
        else:
            total += 1
            direction *= -1
    a += direction
    b -= direction

print(f'{a}/{b}')