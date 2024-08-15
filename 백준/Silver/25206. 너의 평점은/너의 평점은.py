N = 20
total_points = 0
total_grade = 0

for _ in range(N):
    name, points, grade = input().split()

    if grade == 'P':
        continue

    points = int(float(points))
    grade_num = 0

    total_points += points
    
    if 'A' in grade:
        grade_num += 4
    elif 'B' in grade:
        grade_num += 3
    elif 'C' in grade:
        grade_num += 2
    elif 'D' in grade:
        grade_num += 1
    
    if '+' in grade:
        grade_num += 0.5
    
    total_grade += points * grade_num

if total_points:
    print(f'{total_grade / total_points:0.6f}')
else:
    print(0)