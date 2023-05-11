def solution(enroll, referral, seller, amount):
    answer = []
    length = len(enroll)
    s_length = len(seller)
    
    dic = dict()
    
    for i in range(length):
        dic[enroll[i]] = [0, referral[i]]
    
    for i in range(s_length):
        s = seller[i]
        a = amount[i] * 100
        
        while s != '-' and a > 0:
            fee = a // 10
            mine = a - fee
            dic[s][0] += mine
            s = dic[s][1]
            a = fee
    
    for name in enroll:
        answer.append(dic[name][0])
    
    return answer