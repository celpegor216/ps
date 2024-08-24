lst1 = [int(input()) for _ in range(4)]
lst2 = [int(input()) for _ in range(2)]

print(sum(lst1) - min(lst1) + sum(lst2) - min(lst2))