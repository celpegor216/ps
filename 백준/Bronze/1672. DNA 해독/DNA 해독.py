N = int(input())
S = input()

table = [
    'ACAG',
    'CGTA',
    'ATCG',
    'GAGT'
]
char_to_idx = {'A': 0, 'G': 1, 'C': 2, 'T': 3}

result = S[-1]
for n in range(N - 2, -1, -1):
    i, j = char_to_idx[S[n]], char_to_idx[result]
    result = table[i][j]

print(result)