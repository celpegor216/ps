N = int(input())
pattern = input()
length = len(pattern)
start = pattern.index('*')
end = length - start
lst = [input() for _ in range(N)]

for n in range(N):
    if len(lst[n]) >= length - 1 and lst[n][:start] == pattern[:start] and lst[n][-end + 1:] == pattern[-end + 1:]:
        print('DA')
    else:
        print('NE')