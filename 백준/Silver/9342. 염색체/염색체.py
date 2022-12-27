T = int(input())

lst = list('ABCDEF')

def check(word):
    check_A = False

    idx = 0

    # 문자열은 {A, B, C, D, E, F} 중 0개 또는 1개로 시작해야 한다.
    now = word[idx]
    if now == 'A':
        check_A = True
    elif now not in lst:
        return 0

    idx += 1

    # 그 다음에는 A가 하나 또는 그 이상 있어야 한다.
    while idx < len(word):
        now = word[idx]
        if check_A:
            if now == 'F':
                idx += 1
                break
            elif now != 'A':
                return 0
            idx += 1
        else:
            if now == 'A':
                check_A = True
                idx += 1
            else:
                return 0

    if idx == len(word):
        return 0

    # 그 다음에는 F가 하나 또는 그 이상 있어야 한다.
    while idx < len(word):
        now = word[idx]
        if now == 'C':
            idx += 1
            break
        elif now != 'F':
            return 0
        idx += 1

    if now != 'C':
        return 0

    # 그 다음에는 C가 하나 또는 그 이상 있어야 한다.
    # 그 다음에는 {A, B, C, D, E, F} 중 0개 또는 1개가 있으며, 더 이상의 문자는 없어야 한다.
    while idx < len(word):
        now = word[idx]
        if now == 'C':
            idx += 1
        elif now in lst:
            return 1
        else:
            return 0

    return 1

for t in range(T):
    s = input()

    result = check(s)

    if not result:
        print('Good')
    else:
        print('Infected!')