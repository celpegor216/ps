def solution(rank, attendance):
    temp = sorted([[rank[i], i] for i in range(len(rank)) if attendance[i]], key = lambda x : x[0])
    
    return temp[0][1] * 10000 + temp[1][1] * 100 + temp[2][1]