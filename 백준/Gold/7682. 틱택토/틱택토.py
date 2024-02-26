result = set()
used = [0] * 9

def add_result():
    tmp = ''
    for i in range(9):
        if used[i] == 1:
            tmp += 'X'
        elif used[i] == -1:
            tmp += 'O'
        else:
            tmp += '.'
    result.add(tmp)

def check():
    for i in range(3):
        if abs(sum(used[i * 3:(i + 1) * 3])) == 3:
            return True

        if abs(used[i] + used[i + 3] + used[i + 6]) == 3:
            return True

    if abs(used[0] + used[4] + used[8]) == 3:
        return True

    if abs(used[2] + used[4] + used[6]) == 3:
        return True

    return False         

def make(level, now):
    if check() or level == 9:
        add_result()
        return

    for i in range(9):
        if not used[i]:
            used[i] = now
            make(level + 1, -now)
            used[i] = 0

make(0, 1)

while 1:
    S = input()

    if S == "end":
        break

    print("valid" if S in result else "invalid")