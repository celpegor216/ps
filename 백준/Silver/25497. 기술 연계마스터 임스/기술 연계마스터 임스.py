N = int(input())
S = input()

cnt_L = cnt_S = 0
result = 0
for i in range(N):
    if S[i].isdigit():
        result += 1
    elif S[i] == 'L':
        cnt_L += 1
    elif S[i] == 'S':
        cnt_S += 1
    elif S[i] == 'R':
        if not cnt_L:
            break
        cnt_L -= 1
        result += 1
    elif S[i] == 'K':
        if not cnt_S:
            break
        cnt_S -= 1
        result += 1

print(result)