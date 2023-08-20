S = input()
lst = [S[x:] for x in range(len(S))]

lst.sort()

for item in lst:
    print(item)