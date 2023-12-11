S = input()

result = ''
cnt = 0

for i in range(len(S)):
    if S[i] == 'X':
        cnt += 1
    else:
        if cnt > 0 and cnt % 2:
            result = '-1'
            cnt = 0
            break
        else:
            while cnt:
                if cnt >= 4:
                    result += 'AAAA'
                    cnt -= 4
                else:
                    result += 'BB'
                    cnt -= 2
        result += '.'


if cnt > 0 and cnt % 2:
    result = '-1'
else:
    while cnt:
        if cnt >= 4:
            result += 'AAAA'
            cnt -= 4
        else:
            result += 'BB'
            cnt -= 2

print(result)