S = input()

char_to_num = {
    'ABC': 3,
    'DEF': 4,
    'GHI': 5,
    'JKL': 6,
    'MNO': 7,
    'PQRS': 8,
    'TUV': 9,
    'WXYZ': 10,
}

result = 0
for s in S:
    for key in char_to_num.keys():
        if s in key:
            result += char_to_num[key]
            break

print(result)