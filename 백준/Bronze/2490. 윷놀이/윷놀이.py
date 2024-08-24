N = 3
lst = 'DCBAE'

for _ in range(N):
    num = sum(map(int, input().split()))

    print(lst[num])