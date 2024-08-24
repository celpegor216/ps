A, B = map(int, input().split())
C = int(input())

total = A * 60 + B + C

print((total // 60) % 24, total % 60)