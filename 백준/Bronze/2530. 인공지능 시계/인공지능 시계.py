A, B, C = map(int, input().split())
D = int(input())

minute = 60
hour = minute ** 2
total = A * hour + B * minute + C + D

print((total // hour) % 24, (total // minute) % 60, total % 60)