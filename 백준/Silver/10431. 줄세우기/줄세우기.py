for _ in range(int(input())):
    lst = list(map(int, input().split()))
  
    result = 0

    for i in range(2, 21):
        for j in range(i, 1, -1):
            if lst[j - 1] > lst[j]:
                result += 1
                lst[j], lst[j - 1] = lst[j - 1], lst[j]

    print(lst[0], result)