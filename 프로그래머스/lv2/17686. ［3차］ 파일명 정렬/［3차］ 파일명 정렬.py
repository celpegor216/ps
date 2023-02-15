def solution(files):
    answer = []
    
    fs = []
    for i in range(len(files)):
        cut = -1
        temp = []
        for j in range(len(files[i])):
            if cut < 0 and '0' <= files[i][j] <= '9':
                cut = j
                temp.append(files[i][:j].lower())
            elif cut > 0 and not '0' <= files[i][j] <= '9':
                temp.append(int(files[i][cut:j]))
                temp.append(files[i][j:])
                cut = -2
                break
        if cut != -2:
            temp.append(int(files[i][cut:]))
            temp.append('')
        temp.append(i)
        fs.append(temp)
    
    fs.sort(key = lambda x: (x[0], x[1], x[3]))
    
    for i in range(len(fs)):
        answer.append(files[fs[i][3]])
    
    return answer