s = input()
length = len(s)

maxv = ''
minv = ''

temp = 0
for i in range(length):
    if s[i] == 'K':
        maxv += str(5 * 10 ** (i - temp))
        temp = i + 1
if temp != length:
    maxv += '1' * (length - temp)
print(maxv)

temp = 0
for i in range(length):
    if s[i] == 'K':
        if i > temp:
            minv += str(10 ** (i - temp - 1))
        minv += '5'
        temp = i + 1
if temp != length:
    minv += str(10 ** (length - temp - 1))
print(minv)