A, B = map(int, input().split())

side = 0
while A < 5 and B < 5:
    if not side:
        B += A
    else:
        A += B
    side = 1 - side

print('yt' if B >= 5 else 'yj')