def solution(today, terms, privacies):
    answer = []
    
    today = int(today[:4]) * 12 * 28 + int(today[5:7]) * 28 + int(today[8:])
    
    dic = {}
    for term in terms:
        a, b = term.split()
        dic[a] = int(b)
        
    for i in range(len(privacies)):
        date, term = privacies[i].split()
        
        date = int(date[:4]) * 12 * 28 + (int(date[5:7]) + dic[term]) * 28 + int(date[8:])
        
        if today >= date:
            answer.append(i + 1)
    
    return answer