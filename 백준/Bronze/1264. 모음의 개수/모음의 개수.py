vowels = 'aeiou'

while 1:
    S = input().lower()

    if S == '#':
        break

    result = 0
    for vowel in vowels:
        result += S.count(vowel)

    print(result)