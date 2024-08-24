TC = int(input())

for _ in range(TC):
    S = input()

    now = 0
    result = 0

    for s in S:
        if s == 'O':
            now += 1
            result += now
        else:
            now = 0
    
    print(result)