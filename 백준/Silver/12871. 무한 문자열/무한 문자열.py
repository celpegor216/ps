S = input()
T = input()

S, T = S * len(T), T * len(S)

flag = 1
for i in range(len(S)):
    if S[i] != T[i]:
        flag = 0
        break

print(flag)