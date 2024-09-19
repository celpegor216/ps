N = int(input())
lst = list(map(int, input().split()))

result = 0

while len(lst) > 1:
    lst.sort()

    time = lst.pop(-2)
    result += time
    lst[-1] -= time

result += lst[0]
print(result if result <= 1440 else -1)