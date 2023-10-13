N = int(input())
lst = list(map(int, input().split()))

money_A, money_B = N, N
stock_A, stock_B = 0, 0
A, B = 0, 0

for item in lst:
    if item <= money_A:
        cnt = money_A // item
        money_A -= cnt * item
        stock_A += cnt

isIncrease = 0

for i in range(len(lst)):
    if i > 0:
        if lst[i] > lst[i - 1]:
            if isIncrease > 0:
                isIncrease += 1
            else:
                isIncrease = 1
        elif lst[i] < lst[i - 1]:
            if isIncrease < 0:
                isIncrease -= 1
            else:
                isIncrease = -1
        else:
            isIncrease = 0
    
    if isIncrease >= 3:
        money_B += stock_B * lst[i]
        stock_B = 0
    elif isIncrease <= -3:
        cnt = money_B // lst[i]
        money_B -= cnt * lst[i]
        stock_B += cnt

A = money_A + stock_A * lst[-1]
B = money_B + stock_B * lst[-1]

if A > B:
    print("BNP")
elif A < B:
    print("TIMING")
else:
    print("SAMESAME")