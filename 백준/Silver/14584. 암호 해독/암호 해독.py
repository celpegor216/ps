S = input()
N = int(input())
lst = [input() for _ in range(N)]

# 정답을 찾으면 바로 종료하기 위해 함수 사용
def find():
    for k in range(26):
        # S의 모든 글자를 하나씩 알파벳 순서에서 오른쪽으로 밀어서 새로운 문자열을 생성
        new_S = ''.join([chr((ord(s) + k) % 26 + ord('a')) for s in S])

        # 만약 사전에 있는 단어 중 하나라도 새로운 문자열에 있다면
        # 해당 문자열이 정답
        for item in lst:
            if item in new_S:
                return new_S

print(find())