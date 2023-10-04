dic = dict()
total = 0

while 1:
    try:
        name = input()

        total += 1
        if dic.get(name):
            dic[name] += 1
        else:
            dic[name] = 1
    except:
        break

for item in sorted(dic.items()):
    print(item[0], f'{item[1] / total * 100:0.4f}')