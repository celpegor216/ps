T = int(input())

for t in range(T):
    s = input().split()

    dic = dict()
    while 1:
        temp = input().split()

        if len(temp) > 3:
            break
        
        dic[temp[2]] = temp[0]
    
    for i in range(len(s)):
        if s[i] in dic.keys():
            s[i] = ''
    
    result = ''

    for item in s:
        if item:
            result += item + ' '
    
    print(result)