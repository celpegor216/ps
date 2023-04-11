def solution(genres, plays):
    dic = {}
    length = len(genres)
    
    for i in range(length):
        if dic.get(genres[i]):
            dic[genres[i]][0] += plays[i]
            dic[genres[i]].append([i, plays[i]])
        else:
            dic[genres[i]] = [plays[i], [i, plays[i]]]
    
    lst = list(dic.items())
    lst.sort(key=lambda x: -x[1][0])
    
    answer = []
    
    for item in lst:
        temp = sorted(item[1][1:], key=lambda x: -x[1])[:2]
        for t in temp:
            answer.append(t[0])
    
    return answer