N = int(input())
ins = [input() for _ in range(N)]
outs = [input() for _ in range(N)]

result = 0
inp = 0
outp = 0

not_used = []

while outp < N:
    if ins[inp] == outs[outp]:
        inp += 1
        outp += 1
    else:
        if ins[inp] in not_used:
            not_used.remove(ins[inp])
            inp += 1
        else:
            not_used.append(outs[outp])
            outp += 1
            result += 1

print(result)