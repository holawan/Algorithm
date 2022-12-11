import sys


# 회문인지 판단
def solution(n):
    # 문자열이 짝수인지 홀수인지에 따라서 왼쪽 문자열과 오른쪽 문자열을 나눔.
    if len(word) % 2 == 0:
        left = word[0: len(word)//2 - n]
    else:
        left = word[0: len(word)//2 + 1 - n]

    right = word[len(word)//2:len(word) - n]

    # 왼쪽 문자열과 오른쪽 문자열이 똑같지 않으면 회문이 아님
    if left != right[::-1]:
        return True
    return False


word = list(map(str, sys.stdin.readline().strip()))

# 길이 n이 회문인지 확인
if solution(0):
    print(len(word))

# 길이 n-1이 회문인지 확인
elif solution(1):
    print(len(word) - 1)

# 회문!!!
else:
    print(-1)