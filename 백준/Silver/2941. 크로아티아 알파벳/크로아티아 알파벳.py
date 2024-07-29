S = input()
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for item in lst:
    S = S.replace(item, ' ')

print(len(S))