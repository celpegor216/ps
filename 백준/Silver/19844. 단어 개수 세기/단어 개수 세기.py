S = input().replace('-', ' ').split()

vowels = 'aeiouh'
starts = ["c'", "j'", "n'", "m'", "t'", "s'", "l'", "d'", "qu'"]

result = 0
for s in S:
    result += 1
    for start in starts:
        if s.startswith(start) and s[len(start)] in vowels:
            result += 1
            break

print(result)