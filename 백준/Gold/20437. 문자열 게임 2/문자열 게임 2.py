T = int(input())

for t in range(T):
    W = input()
    K = int(input())

    dic = dict()

    for i in range(len(W)):
        if dic.get(W[i]):
            dic[W[i]].append(i)
        else:
            dic[W[i]] = [i]
    
    short = 21e8
    long = -1

    for key in dic.keys():
        length = len(dic[key])
        if length >= K:
            for i in range(length - K + 1):
                if dic[key][i + K - 1] - dic[key][i] < short:
                    short = dic[key][i + K - 1] - dic[key][i]
                
                if dic[key][i + K - 1] - dic[key][i] > long:
                    long = dic[key][i + K - 1] - dic[key][i]
    
    if short == 21e8 or long == -1:
        print(-1)
    else:
        print(short + 1, long + 1)