name = input()

result = 'Error!'

# C++
if '_' in name:
    flag = 0

    for s in name:
        if 'A' <= s <= 'Z':
            flag = 1
            break
    
    tmp = name.split('_')

    for item in tmp:
        if not item:
            flag = 1
            break

    if not flag:
        result = ''
        
        for i in range(len(tmp)):
            if i == 0:
                result += tmp[i]
            else:
                result += tmp[i][0].upper() + tmp[i][1:]
else:
    flag = 0

    if 'A' <= name[0] <= 'Z':
        flag = 1

    if not flag:
        result = ''
        for n in name:
            if 'a' <= n <= 'z':
                result += n
            else:
                result += '_' + n.lower()

print(result)