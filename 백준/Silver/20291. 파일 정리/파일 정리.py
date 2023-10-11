import sys
input = sys.stdin.readline

dic = dict()

for _ in range(int(input())):
    name, file_type = input().split('.')

    if dic.get(file_type):
        dic[file_type] += 1
    else:
        dic[file_type] = 1
    
for key, value in sorted(dic.items()):
    print(key.strip(), value)