S = input()

scores = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0, '+': 0.3, '-': -0.3, '0': 0}

result = 0
for s in S:
    result += scores[s]

print(f'{result:0.1f}')