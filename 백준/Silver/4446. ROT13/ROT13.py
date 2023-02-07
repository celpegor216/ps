while 1:
    try:
        S = input()

        result = ''

        vowels = list('aiyeou')
        consonants = list('bkxznhdcwgpvjqtsrlmf')

        for s in S:
            if s.isalpha():
                temp = s.lower()
                if temp in vowels:
                    if 'A' <= s <= 'Z':
                        result += vowels[(vowels.index(temp) + 3) % 6].upper()
                    else:
                        result += vowels[(vowels.index(temp) + 3) % 6]
                elif temp in consonants:
                    if 'A' <= s <= 'Z':
                        result += consonants[(consonants.index(temp) + 10) % 20].upper()
                    else:
                        result += consonants[(consonants.index(temp) + 10) % 20]
            else:
                result += s

        print(result)
    except:
        break