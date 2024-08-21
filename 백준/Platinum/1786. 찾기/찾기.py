# 해답: https://velog.io/@rhdmstj17/KMP-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-python-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%83%90%EC%83%89-%EA%B0%80%EC%9E%A5-%EC%89%BD%EA%B2%8C-%EC%9D%B4%ED%95%B4%ED%95%B4%EB%B3%B4%EA%B8%B0


T = input()
P = input()

length_T = len(T)
length_P = len(P)

# k에서 매칭이 실패했을 때 다음 탐색에서 시작할 인덱스
jump = [0] * length_P
i = 0    # 접두사
for j in range(1, length_P):    # 접미사
    while i and P[i] != P[j]:
        i = jump[i - 1]

    if P[i] == P[j]:
        i += 1
        jump[j] = i

result = []

j = 0    # 탐색중인 패턴 인덱스
for i in range(length_T):
    while j and T[i] != P[j]:
        j = jump[j - 1]

    if T[i] == P[j]:
        if j == length_P - 1:
            result.append(i - length_P + 2)
            j = jump[j]
        else:
            j += 1

print(len(result))
if result:
    print(*result)