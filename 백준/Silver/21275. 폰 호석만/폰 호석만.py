a, b = input().split()
a = a[::-1]
b = b[::-1]

a_min = 36
b_min = 36

for s in a:
    if '0' <= s <= '9':
        a_min = min(a_min, int(s))
    else:
        a_min = min(a_min, 10 + ord(s) - ord('a'))

for s in b:
    if '0' <= s <= '9':
        b_min = min(b_min, int(s))
    else:
        b_min = min(b_min, 10 + ord(s) - ord('a'))

lst_a = [-1] * 37
lst_b = [-1] * 37

for i in range(2, 36):
    temp_a = 0
    temp_b = 0

    if a_min < i:
        now = 1
        for s in a:
            if '0' <= s <= '9':
                temp_a += int(s) * now
            else:
                temp_a += (10 + ord(s) - ord('a')) * now
            now *= i
    else:
        temp_a = -1
    
    if b_min < i:
        now = 1
        for s in b:
            if '0' <= s <= '9':
                temp_b += int(s) * now
            else:
                temp_b += (10 + ord(s) - ord('a')) * now
            now *= i
    else:
        temp_b = -1
    
    if temp_a < 2 ** 63:
        lst_a[i] = temp_a

    if temp_b < 2 ** 63:
        lst_b[i] = temp_b

result = []

for i in range(2, 36):
    for j in range(2, 36):
        if lst_a[i] == lst_b[j] and lst_a[i] != -1:
            result.append([lst_a[i], i, j])

if not result:
    print('Impossible')
elif len(result) == 1:
    print(*result[0])
else:
    print('Multiple')