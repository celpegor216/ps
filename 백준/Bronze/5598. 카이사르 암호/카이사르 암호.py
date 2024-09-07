S = input()
for s in S:
    print(chr((ord(s) - ord('A') - 3) % 26 + ord('A')), end='')