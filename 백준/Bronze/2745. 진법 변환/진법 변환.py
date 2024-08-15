N, B = input().split()
B = int(B)

result = 0

length = len(N)

for i in range(length):
    if N[i].isdigit():
        result += B ** (length - i - 1) * int(N[i])
    else:
        result += B ** (length - i - 1) * (10 + ord(N[i]) - ord('A'))

print(result)