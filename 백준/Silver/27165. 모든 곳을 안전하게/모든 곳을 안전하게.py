N = int(input())
lst = list(map(int, input().split()))
dice = int(input())


def find():
    ones = []
    not_ones = []
    for n in range(N + 1):
        if lst[n] == 1:
            ones.append(n)
        elif lst[n] > 2 and n + dice <= N and lst[n + dice] != 0:
            not_ones.append(n)

    length = len(ones)

    if length > 2:
        return 'NO', []
    
    elif length == 0:
        if not_ones:
            return 'YES', [not_ones[0], not_ones[0] + dice]
        return 'NO', []
    
    elif length == 2:
        if ones[-1] - ones[0] != dice:
            return 'NO', []
        return 'YES', ones[:]

    else:
        if ones[0] + dice <= N and lst[ones[0] + dice]:
            return 'YES', [ones[0], ones[0] + dice]
        elif ones[0] - dice >= 0 and lst[ones[0] - dice] > 2:
            return 'YES', [ones[0] - dice, ones[0]]
        return 'NO', []

result, positions = find()


print(result)
if positions:
    print(*positions)