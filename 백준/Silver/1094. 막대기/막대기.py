N = int(input())

if N == 64:
    print(1)
else:
    total = 0
    now = 64
    result = 0

    while total < N:
        half = now // 2
        if total + half <= N:
            result += 1
            total += half
        now = half

    print(result)