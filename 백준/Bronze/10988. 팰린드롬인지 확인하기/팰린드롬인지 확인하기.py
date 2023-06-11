s = input()

while s:
    if s[0] == s[-1]:
        s = s[1:-1]
    else:
        break

if s:
    print(0)
else:
    print(1)