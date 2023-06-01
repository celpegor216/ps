s, n = input().split()
s = int(s)
length = 2 * s + 3

result = [''] * length

for num in n:
    for i in range(length):
        if i == 0:
            if num in '14':
                result[i] += ' ' * (s + 3)
            else:
                result[i] += ' ' + '-' * s + ' ' * 2
        elif 0 < i < s + 1:
            if num in '1237':
                result[i] += ' ' * (s + 1) + '| '
            elif num in '56':
                result[i] += '|' + ' ' * (s + 2)
            else:
                result[i] += '|' + ' ' * s + '| '
        elif i == s + 1:
            if num in '170':
                result[i] += ' ' * (s + 3)
            else:
                result[i] += ' ' + '-' * s + ' ' * 2
        elif s + 1 < i < 2 * s + 2:
            if num in '134579':
                result[i] += ' ' * (s + 1) + '| '
            elif num in '2':
                result[i] += '|' + ' ' * (s + 2)
            else:
                result[i] += '|' + ' ' * s + '| '
        else:
            if num in '147':
                result[i] += ' ' * (s + 3)
            else:
                result[i] += ' ' + '-' * s + ' ' * 2

for line in result:
    print(line)