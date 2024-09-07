dic = {'A': [0, 1], 'B': [1, 2], 'C': [0, 2]}
cups = [1, 0, 0]

S = input()
for s in S:
    cups[dic[s][0]], cups[dic[s][1]] = cups[dic[s][1]], cups[dic[s][0]]

print(cups.index(1) + 1)