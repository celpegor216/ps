M, D = map(int, input().split())

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for m in range(M - 1):
    D += month[m]

days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

print(days[(D - 1) % 7])