N = int(input())

fibo = [0, 1]

if N < 2:
    print(fibo[N])
else:
    for n in range(2, N + 1):
        fibo.append(fibo[n - 2] + fibo[n - 1])
    
    print(fibo[-1])