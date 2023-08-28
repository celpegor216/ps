vowels = 'aeiou'

while 1:
    s = input()

    if s == 'end':
        break

    check_vowel = 0
    
    for vowel in vowels:
        if vowel in s:
            check_vowel = 1
            break
    
    flag = 0
    if not check_vowel:
        flag = 1
    else:
        now = ''
        now_cnt = 0
        type_cnt = 0

        for i in range(len(s)):
            if s[i] == now:
                now_cnt += 1
                type_cnt += 1
            elif (s[i] in vowels and now in vowels) or (s[i] not in vowels and now not in vowels):
                now = s[i]
                now_cnt = 1
                type_cnt += 1
            else:
                now = s[i]
                now_cnt = 1
                type_cnt = 1
            
            if (now not in 'eo' and now_cnt > 1) or type_cnt > 2:
                flag = 1
                break
    
    if flag:
        print(f'<{s}> is not acceptable.')
    else:
        print(f'<{s}> is acceptable.')