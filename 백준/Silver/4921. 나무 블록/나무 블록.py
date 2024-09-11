# i번 조각의 오른쪽에 올 수 있는 조각들
possible_rights = {
    '1': '45',
    '2': '',
    '3': '45',
    '4': '23',
    '5': '8',
    '6': '23',
    '7': '8',
    '8': '67'
}

def check():
    # 가장 왼쪽 조각은 1번 조각, 가장 오른쪽 조각은 2번 조각이어야 한다.
    if S[0] != '1' or S[-1] != '2':
        return 0

    # 1번 조각의 왼쪽과 2번 조각의 오른쪽에 맞물리는 조각은 없다.
    # 각각의 1번 조각에 대해서, 대응하는 2번 조각이 있어야 하고,
    # 5번 조각에 대해서도 대응하는 6번 조각이 있어야 한다.
    cnt_5 = 0

    # 인접한 조각은 서로 맞물려야 한다.
    # 예를 들어, 4번 조각과 5번 조각은 항상 1번 조각의 오른쪽에 있어야 한다.
    # 또, 4번 조각은 1번이나 3번조각의 오른쪽에 있을 수 있다.
    for i in range(len(S) - 1):
        if S[i + 1] not in possible_rights[S[i]]:
            return 0

        if S[i + 1] == '5':
            cnt_5 += 1
        elif S[i + 1] == '6':
            if not cnt_5:
                return 0
            cnt_5 -= 1

    return 1


tc = 0
while 1:
    tc += 1

    S = input()

    if S == '0':
        break

    print(f"{tc}. {'VALID' if check() else 'NOT'}")