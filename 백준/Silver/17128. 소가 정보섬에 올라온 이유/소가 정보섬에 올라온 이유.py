N, Q = map(int, input().split())
lst_n = list(map(int, input().split()))
lst_q = list(map(int, input().split()))

lst = [0] * N

for n in range(N):
    lst[n] = lst_n[n % N] * lst_n[(n + 1) % N] * lst_n[(n + 2) % N] * lst_n[(n + 3) % N]

total = sum(lst)

for q in lst_q:
    q -= 1
    
    for i in range(4):
        lst[(q - i) % N] *= -1
        total += lst[(q - i) % N] * 2
    
    print(total)