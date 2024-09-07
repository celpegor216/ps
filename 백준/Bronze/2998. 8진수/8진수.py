binary = input()
if len(binary) % 3:
    binary = '0' * (3 - len(binary) % 3) + binary

result = ''
for i in range(0, len(binary), 3):
    result += str(int(binary[i:i + 3], 2))

print(result)