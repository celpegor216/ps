import sys
input = sys.stdin.readline

K, L = map(int, input().split())
dic = dict()

for l in range(1, L + 1):
    student_id = int(input())
    dic[student_id] = l

for key, value in sorted(dic.items(), key=lambda x: x[1])[:K]:
    print(f'{key:08d}')
