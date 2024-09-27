# 틀린 부분 진심 어딘지 모르겠음
# 해답: https://velog.io/@hyun0820/%EB%B0%B1%EC%A4%80-3425-%EA%B3%A0%EC%8A%A4%ED%83%9D



def calculate(command, num):
    go = [num]
    for i in command:
        # X를 스택의 가장 위에 저장
        if "NUM" in i:
            go.append(int(i.split()[1]))
        # 스택의 가장 위의 숫자를 제거
        elif go and i == "POP":
            go.pop()
        # 첫 번째 수의 부호를 바꿈
        elif go and i == "INV":
            go[-1] = go[-1] * (-1)
        # 첫 번째 숫자를 하나 더 저장
        elif go and i == "DUP":
            go.append(go[-1])
        # 첫 번째 숫자와 두 번째 숫자의 위치를 서로 바꿈
        elif len(go) > 1 and i == "SWP":
            tmp = go.pop() # 첫 번째 원소
            tmp2 = go.pop() # 두 번째 원소
            go.append(tmp)
            go.append(tmp2)
        # 두 번째 원소 + 첫 번째 원소
        elif len(go) > 1 and i == "ADD":
            data1 = go.pop() # 첫 번째 원소
            data2 = go.pop() # 두 번째 원소
            answer = data2 + data1
            if abs(answer) > 10 ** 9:
                return "ERROR"
            go.append(answer)
        # 두 번째 원소 - 첫 번째 원소
        elif len(go) > 1 and i == "SUB":
            data1 = go.pop() # 첫 번째 원소
            data2 = go.pop() # 두 번째 원소
            answer = data2-data1
            if abs(answer) > 10 ** 9:
                return "ERROR"
            go.append(answer)
        # 두 번째 원소 * 첫 번째 원소
        elif len(go) > 1 and i == "MUL":
            data1 = go.pop()
            data2 = go.pop()
            answer = data2 * data1
            if abs(answer) > 10 ** 9:
                return "ERROR"
            go.append(answer)
        # 두 번째 원소 // 첫 번째 원소
        elif len(go) > 1 and i == "DIV":
            data1 = go.pop()
            data2 = go.pop()
            if data1 == 0:
                return "ERROR"
            answer = abs(data2) // abs(data1)
            if (data1 * data2) < 0 :
                answer = (-1) * answer
            if abs(answer) > 10 ** 9:
                return "ERROR"
            go.append(answer)
        # 두 번째 원소 % 첫 번째 원소
        elif len(go) > 1 and i == "MOD":
            data1 = go.pop()
            data2 = go.pop()
            if data1 == 0:
                return "ERROR"
            answer = abs(data2) % abs(data1)
            if data2 < 0:
                answer = (-1) * answer
            if abs(answer) > 10 ** 9 :
                return "ERROR"
            go.append(answer)
        else :
            return "ERROR"
    if len(go) == 1:
        return go.pop()
    return "ERROR"


while 1:
    command = []
    while 1:
        c = input()
        # 새로운 command 받아오기
        if c == 'END':
            break
        # 프로그램 종료
        if c == 'QUIT':
            quit()
        command.append(c)

    count = int(input()) # 반복 횟수
    for _ in range(count):
        num = int(input())
        print(calculate(command,num))
    # 한 줄 띄우기
    print()
    # 다음 프로그램 시작
    input()