K = int(input())

n = 1    # 자리 수
tmp = K

while 1:
    tmp -= 2 ** n

    if tmp <= 0:
        break
    
    n += 1

left = (K + 1) - (2 ** n)

result = [0] * n

while left:
    n -= 1
    result[n] = left % 2
    left //= 2

for item in result:
    print(7 if item else 4, end='')