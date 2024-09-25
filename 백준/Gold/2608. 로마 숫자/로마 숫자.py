A = input()
B = input()

def rome_to_arab(S):
    total = 0
    idx = 0
    N = len(S)
    while idx < N:
        if S[idx] == 'M':
            total += 1000
            idx += 1
        elif S[idx] == 'C':
            if idx + 1 < N:
                if S[idx + 1] == 'M':
                    total += 900
                    idx += 2
                    continue
                elif S[idx + 1] == 'D':
                    total += 400
                    idx += 2
                    continue
            total += 100
            idx += 1
        elif S[idx] == 'X':
            if idx + 1 < N:
                if S[idx + 1] == 'C':
                    total += 90
                    idx += 2
                    continue
                elif S[idx + 1] == 'L':
                    total += 40
                    idx += 2
                    continue
            total += 10
            idx += 1
        elif S[idx] == 'I':
            if idx + 1 < N:
                if S[idx + 1] == 'X':
                    total += 9
                    idx += 2
                    continue
                elif S[idx + 1] == 'V':
                    total += 4
                    idx += 2
                    continue
            total += 1
            idx += 1
        elif S[idx] == 'V':
            total += 5
            idx += 1
        elif S[idx] == 'L':
            total += 50
            idx += 1
        elif S[idx] == 'D':
            total += 500
            idx += 1

    return total

def arab_to_rome(N):
    res = ''
    while N:
        if N >= 1000:
            num = N // 1000
            res += 'M' * num
            N %= 1000
        elif N >= 100:
            num = N // 100
            if num == 5:
                res += 'D'
            elif num == 9:
                res += 'CM'
            elif num == 1:
                res += 'C'
            elif num == 4:
                res += 'CD'
            elif 1 <= num <= 3:
                res += 'C' * num
            else:
                res += 'D' + 'C' * (num - 5)
            N %= 100
        elif N >= 10:
            num = N // 10
            if num == 5:
                res += 'L'
            elif num == 9:
                res += 'XC'
            elif num == 1:
                res += 'X'
            elif num == 4:
                res += 'XL'
            elif 1 <= num <= 3:
                res += 'X' * num
            else:
                res += 'L' + 'X' * (num - 5)
            N %= 10
        else:
            num = N
            if num == 5:
                res += 'V'
            elif num == 9:
                res += 'IX'
            elif num == 1:
                res += 'I'
            elif num == 4:
                res += 'IV'
            elif 1 <= num <= 3:
                res += 'I' * num
            else:
                res += 'V' + 'I' * (num - 5)
            break
    return res

total = rome_to_arab(A) + rome_to_arab(B)
print(total)
print(arab_to_rome(total))