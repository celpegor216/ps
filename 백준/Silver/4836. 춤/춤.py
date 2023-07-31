while 1:
    try:
        S = input().split()
        N = len(S)

        flags = [0] * 5
        dips = []

        if S[-3:] != ['clap', 'stomp', 'clap']:
            flags[1] = 1

        if 'twirl' in S and 'hop' not in S:
            flags[2] = 1
        
        if S[0] == 'jiggle':
            flags[3] = 1

        if 'dip' not in S:
            flags[4] = 1
        else:
            for n in range(N):
                if S[n] == 'dip':
                    if (n > 0 and S[n - 1] == 'jiggle') or (n > 1 and S[n - 2] == 'jiggle') or (n < N - 1 and S[n + 1] == 'twirl'):
                        continue
                    else:
                        dips.append(n)
            
            if dips:
                flags[0] = 1
        
        if not sum(flags):
            print(f'form ok:', end='')
        elif sum(flags) == 1:
            print(f'form error {flags.index(1) + 1}:', end='')
        else:
            print('form errors', end='')

            errors = [x for x in range(5) if flags[x]]
            for i in range(len(errors)):
                if i == len(errors) - 1:
                    print(f' and {errors[i] + 1}:', end='')
                elif i != 0:
                    print(f', {errors[i] + 1}', end='')
                else:
                    print(f' {errors[i] + 1}', end='')
        
        for i in range(N):
            if i in dips:
                print(' DIP', end='')
            else:
                print(f' {S[i]}', end='')
        print()
    except:
        break