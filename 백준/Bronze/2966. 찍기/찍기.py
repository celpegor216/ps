N = int(input())
S = input()

lst = [
    ['Adrian', 'ABC', 0],
    ['Bruno', 'BABC', 0],
    ['Goran', 'CCAABB', 0]
]

for n in range(N):
    for i in range(3):
        idx = n % len(lst[i][1])
        if lst[i][1][idx] == S[n]:
            lst[i][-1] += 1

lst.sort(key=lambda x: (-x[-1], x[0]))

print(lst[0][-1])
for i in range(3):
    if i > 0 and lst[i][-1] != lst[i - 1][-1]:
        break
    print(lst[i][0])