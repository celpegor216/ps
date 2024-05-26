S = input()

for s in S:
    if 'A' <= s <= 'Z':
        print(chr((ord('A') + (ord(s) - ord('A') + 13) % 26)), end='')
    elif 'a' <= s <= 'z':
        print(chr((ord('a') + (ord(s) - ord('a') + 13) % 26)), end='')
    else:
        print(s, end='')