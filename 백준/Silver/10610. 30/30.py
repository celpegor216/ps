# 모든 숫자를 사용해야 함,,,


N = input()
bucket = [0] * 10

total = 0
for i in range(10):
    bucket[i] = N.count(str(i))
    total += i * bucket[i]

if not bucket[0] or total % 3:
    print(-1)
else:
    for i in range(9, -1, -1):
        print(str(i) * bucket[i], end='')