S = input()
N = int(input())
lst = list(map(int, input().split()))

result = -1

temp = ''
for word in S.split():
    temp += word[0].upper()

now = ''
for s in S + temp:
    if s != now:
        if 'A' <= s <= 'Z':
            lst[ord(s) - ord('A')] -= 1
        elif 'a' <= s <= 'z':
            lst[ord(s) - ord('a')] -= 1
        else:
            N -= 1
        now = s

if N >= 0:
    flag = 0

    for i in range(len(lst)):
        if lst[i] < 0:
            flag = 1
            break

    if not flag:
        result = temp
print(result)