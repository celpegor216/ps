N = int(input())

result = 0
while N > 9:
    tmp = 1
    while N:
        tmp *= N % 10
        N //= 10
    N = tmp
    result += 1

print(result)