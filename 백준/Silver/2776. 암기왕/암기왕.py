T = int(input())

for t in range(T):
    N = int(input())
    dic = dict()
    for num in map(int, input().split()):
        dic[num] = 1

    M = int(input())
    for num in map(int, input().split()):
        if dic.get(num):
            print(1)
        else:
            print(0)
