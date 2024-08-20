S = input()

vowels = 'aeiou'
result = 0

for vowel in vowels:
    result += S.count(vowel)

print(result)