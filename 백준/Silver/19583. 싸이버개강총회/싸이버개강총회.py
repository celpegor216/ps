import sys
input = sys.stdin.readline

def time_to_int(time):
    return int(time[:2]) * 60 + int(time[-2:])

S, E, Q = map(time_to_int, input().split())
dic = dict()

while 1:
    try:
        time, name = input().split()
        time = time_to_int(time)
        if 0 <= time <= S:
            dic[name] = 1
        elif E <= time <= Q and name in dic.keys():
            dic[name] = 2
    except:
        print(len([key for key in dic.keys() if dic[key] == 2]))
        break