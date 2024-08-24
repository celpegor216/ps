N = int(input())
lst = [int(input()) for _ in range(N)]

print('Junhee is cute!' if sum(lst) > N // 2 else 'Junhee is not cute!')