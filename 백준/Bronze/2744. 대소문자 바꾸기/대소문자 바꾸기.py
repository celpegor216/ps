S = input()

result = ''

for s in S:
    if 'a' <= s <= 'z':
        result += chr(ord(s) - ord('a') + ord('A'))
    else:
        result += chr(ord(s) + ord('a') - ord('A'))

print(result)