# kmp... 또다시 참고함
# https://velog.io/@rhdmstj17/KMP-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-python-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%83%90%EC%83%89-%EA%B0%80%EC%9E%A5-%EC%89%BD%EA%B2%8C-%EC%9D%B4%ED%95%B4%ED%95%B4%EB%B3%B4%EA%B8%B0

S = input()
P = input()
s = len(S)
p = len(P)

jump = [0] * p
j = 0
for i in range(1, p):
    while j and P[i] != P[j]:
        j = jump[j - 1]

    if P[i] == P[j]:
        j += 1
        jump[i] = j

j = 0
for i in range(s):
    while j and S[i] != P[j]:
        j = jump[j - 1]

    if S[i] == P[j]:
        j += 1

        if j == p:
            print(1)
            break
else:
    print(0)