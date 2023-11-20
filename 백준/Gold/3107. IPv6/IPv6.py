lst = input().split(':')

for i in range(len(lst) - 1):
    if lst[i] == lst[i + 1] == '':
        lst.remove('')
        break

if len(lst) < 8:
    for i in range(len(lst)):
        if lst[i] == '':
            tmp = ['0000'] * (8 - len(lst))
            lst = lst[:i] + tmp + lst[i:]
            break

for i in range(8):
    if len(lst[i]) < 4:
        lst[i] = '0' * (4 - len(lst[i])) + lst[i]

print(':'.join(lst))