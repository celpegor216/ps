N = int(input())

result = [0] * 5

for _ in range(N):
    X, Y = map(int, input().split())

    if X > 0 and Y > 0:
        result[1] += 1
    elif X < 0 and Y > 0:
        result[2] += 1
    elif X < 0 and Y < 0:
        result[3] += 1
    elif X > 0 and Y < 0:
        result[4] += 1
    else:
        result[0] += 1

for i in range(1, 5):
    print(f'Q{i}: {result[i]}')
print(f'AXIS: {result[0]}')