S = input()
N = len(S)

vowels = 'aeiou'

idx = 0
while idx < N:
    print(S[idx], end='')
    
    if S[idx] in vowels:
        idx += 3
    else:
        idx += 1