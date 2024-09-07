T = int(input())

for _ in range(T):
    N = input()
    N = str(int(N) + int(N[::-1]))

    result = 'YES'
    for i in range(len(N) // 2):
        if N[i] != N[- i - 1]:
            result = 'NO'
            break
    print(result)