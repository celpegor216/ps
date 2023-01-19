def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    dic1 = {}
    dic2 = {}
    
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            word = str1[i:i + 2]
            if word in dic1.keys():
                dic1[word] += 1
            else:
                dic1[word] = 1
    
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            word = str2[i:i + 2]
            if word in dic2.keys():
                dic2[word] += 1
            else:
                dic2[word] = 1
    
    same = 0
    diff = 0
    
    for key in dic1.keys():
        if key in dic2.keys():
            same += min(dic1[key], dic2[key])
            diff += max(dic1[key], dic2[key])
        else:
            diff += dic1[key]
    
    for key in dic2.keys():
        if key not in dic1.keys():
            diff += dic2[key]
    
    answer = same / diff if diff != 0 else 1
    
    return (answer * 65536) // 1