N = int(input())
A = input()
B = input()

def find():
    if A[0] != B[0] or A[-1] != B[-1]:
        return 0

    vowel = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
    a = b = ''
    vowel_cnt_a = [0] * 5
    vowel_cnt_b = [0] * 5

    for n in range(N):
        if A[n] in vowel:
            vowel_cnt_a[vowel[A[n]]] += 1
        else:
            a += A[n]

        if B[n] in vowel:
            vowel_cnt_b[vowel[B[n]]] += 1
        else:
            b += B[n]

    if a != b:
        return 0

    for i in range(5):
        if vowel_cnt_a[i] != vowel_cnt_b[i]:
            return 0

    return 1


print('YES' if find() else 'NO')