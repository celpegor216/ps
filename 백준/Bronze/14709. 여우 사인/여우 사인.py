N = int(input())
lst = [sorted(map(int, input().split())) for _ in range(N)]

cnt = 0

for a, b in lst:
    if (a == 1 and b == 3) or (a == 1 and b == 4) or (a == 3 and b == 4):
        cnt += 1
    else:
        cnt = -1
        break

print('Wa-pa-pa-pa-pa-pa-pow!' if cnt == 3 else 'Woof-meow-tweet-squeek')