# 해답 듣고 구현함

T = int(input())

for t in range(T):
    s = input()
    
    flag = 0
    
    while len(s) > 1 and not flag:
        temp = ''
        
        for i in range(1, len(s), 2):
            temp += s[i]
            if s[i - 1] == s[i + 1]:
                flag = 1
                break
        
        if not flag:
            s = temp
    
    if len(s) == 1 and not flag:
        print('YES')
    else:
        print('NO')