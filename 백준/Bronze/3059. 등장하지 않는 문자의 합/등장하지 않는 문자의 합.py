T = int(input())

for _ in range(T):

    S = set(input())

    print(sum([x for x in range(ord('A'), ord('Z') + 1) if chr(x) not in S]))