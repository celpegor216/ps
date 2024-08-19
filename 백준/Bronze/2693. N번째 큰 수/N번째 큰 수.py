T = int(input())

for _ in range(T):
    print(sorted(map(int, input().split()))[-3])