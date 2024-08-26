# 조건에 하나라도 해당하지 않을 경우 바로 반환하기 위해 함수 사용
def check(S):
    vowels = 'aeiou'

    flag = 0

    # 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
    for vowel in vowels:
        if vowel in S:
            flag = 1

    if not flag:
        return

    N = len(S)
    char_types = [0] * N
    for n in range(N):
        # 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
        if n < N - 1 and S[n] not in 'eo' and S[n] == S[n + 1]:
            return
        if S[n] in vowels:
            char_types[n] = 1
        else:
            char_types[n] = 0

    # 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
    cnt = 0
    now = -1
    for n in range(N):
        if char_types[n] == now:
            cnt += 1
        else:
            cnt = 1
            now = char_types[n]

        if cnt > 2:
            return

    return 1


while 1:
    S = input()

    if S == 'end':
        break

    print(f'<{S}> is acceptable.' if check(S) else f'<{S}> is not acceptable.')