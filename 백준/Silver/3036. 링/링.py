N = int(input())
lst = list(map(int, input().split()))

for item in lst[1:]:
    a, b = lst[0], item

    while b > 1:
        a, b = b, a % b

    if not lst[0] % a and not item % a:
        print(f'{lst[0] // a}/{item // a}')
    else:
        print(f'{lst[0]}/{item}')