N, B = map(int, input().split())

result = ''

while N:
    tmp = N % B
    if tmp >= 10:
        tmp = chr(ord('A') + tmp - 10)
    result += str(tmp)
    N //= B

print(result[::-1])