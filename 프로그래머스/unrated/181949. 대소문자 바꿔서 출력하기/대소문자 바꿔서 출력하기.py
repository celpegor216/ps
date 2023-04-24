str = input()

answer = ''

for s in str:
    if 'a' <= s <= 'z':
        answer += s.upper()
    else:
        answer += s.lower()

print(answer)