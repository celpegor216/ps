N = int(input())
dic = dict()

T = int(input())
polls = list(map(int, input().split()))

for t in range(T):
    if polls[t] in dic.keys():
        dic[polls[t]][1] += 1
    else:
        if len(dic.keys()) >= N:
            minv = 21e8
            oldidx = 21e8

            for key in dic.keys():
                if dic[key][1] < minv:
                    minv = dic[key][1]
                    oldidx = key
                elif dic[key][1] == minv and dic[key][0] < dic[oldidx][0]:
                    oldidx = key
            
            dic.pop(oldidx)
        dic[polls[t]] = [t, 1]

print(*sorted(dic.keys()))