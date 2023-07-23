N = int(input())

a, b = 0, 1

for i in range(N - 1):
    temp = (a + b) % 1000000007
    a = b % 1000000007
    b = temp % 1000000007

print(b)