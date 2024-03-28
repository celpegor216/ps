T = int(input())

def check(S):
    for i in range(len(S) // 2):
        if S[i] != S[-i - 1]:
            return i
    return -1

for t in range(T):
    S = input()

    flag = check(S)

    if flag == -1:
        print(0)
    else:
        # 왼쪽 빼고 다시 확인
        c = check(S[:flag] + S[flag + 1:])

        # 오른쪽 빼고 다시 확인
        if c != -1:
            c = check(S[:-flag - 1] + S[len(S) - flag:])
        
        if c == -1:
            print(1)
        else:
            print(2)