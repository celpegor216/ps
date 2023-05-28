T = int(input())

for t in range(T):
    lst = input().split()
    
    print(' '.join([''.join(x[::-1]) for x in lst]))