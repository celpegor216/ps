import sys
input = sys.stdin.readline

N = int(input())
have = list(map(int, input().split()))
want = list(map(int, input().split()))

# 사이클을 이루지 않더라도 그 중 일부는 원하는 수업을 수강할 수 있음
MAX = 10 ** 6

lst = [[] for _ in range(MAX + 1)]
for n in range(N):
    lst[have[n]].append(want[n])

for n in range(1, MAX + 1):
    tmp = []

    for _ in range(len(lst[n])):
        now = lst[n].pop()

        while 1:
            if now == n:
                break
                
            if lst[now]:
                now = lst[now].pop()
            else:
                tmp.append(now)
                break
    
    lst[n] = tmp

print(sum([len(line) for line in lst]))