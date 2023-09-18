T = int(input())

for t in range(T):
    N = int(input())
    now = input()
    target = input()

    changes = [0, 0] # W가 되어야 하는 것 / B가 되어야 하는 것
    for n in range(N):
        if now[n] == 'B' and target[n] == 'W':
            changes[0] += 1
        elif now[n] == 'W' and target[n] == 'B':
            changes[1] += 1
    
    result = 0
    if changes[0] > changes[1]:
        result += changes[0] - changes[1]
        changes[0] = changes[1]
    else:
        result += changes[1] - changes[0]
        changes[1] = changes[0]
    
    print(result + changes[1])