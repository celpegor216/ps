def solution(id_list, report, k):
    # 메일 받은 수 목록
    answer = [0] * len(id_list)
    
    # 신고 받은 사람: 신고한 사람 목록
    dic = {}
    
    for id in id_list:
        dic[id] = set()
    
    for r in report:
        f, t = r.split()
        dic[t].add(f)
    
    for key in dic.keys():
        if len(dic[key]) >= k:
            for p in dic[key]:
                answer[id_list.index(p)] += 1
    
    return answer