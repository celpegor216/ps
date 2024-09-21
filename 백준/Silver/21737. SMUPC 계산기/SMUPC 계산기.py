N = int(input())

cmds = input().replace('S', ' - ').replace('M', ' * ').replace('U', ' / ').replace('P', ' + ').replace('C', ' = ').split()

if cmds[-1] in '+-*/':
    cmds.pop()

N = len(cmds)

results = []

now = int(cmds[0])

n = 1
while n < N:
    if cmds[n] == '+':
        now += int(cmds[n + 1])
        n += 1
    elif cmds[n] == '-':
        now -= int(cmds[n + 1])
        n += 1
    elif cmds[n] == '*':
        now *= int(cmds[n + 1])
        n += 1
    elif cmds[n] == '/':
        nxt = int(cmds[n + 1])
        if now < 0 and nxt > 0:
            now = -(-now // nxt)
        else:
            now //= int(cmds[n + 1])
        n += 1
    elif cmds[n] == '=':
        results.append(now)
    n += 1

if not results:
    print('NO OUTPUT')
else:
    print(*results)