N = int(input())
lst = sorted(map(int, input().split()))

print(sum(lst[:-1]) / 2 + lst[-1])