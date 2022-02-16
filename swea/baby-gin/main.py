import sys
sys.stdin = open("input.txt",'r')

n = int(input())
for x in range(n):
    num = int(input())  # 숫자 입력받기
    c = [0] *12 #숫자별 카운트를 담을 상자
    for i in range(6) : #6자리 숫자만큼
        c[num%10] +=1 #숫자를 10으로 나눈 나머지의 인덱스에 1 추가
                      #해당 숫자를 1카운트 하는 것과 동일
        num //= 10 # 숫자를 10으로 나눈 몫으로 재지정
    i = 0
    tri = run = 0

    while i <10 : #숫자가 10 미만일 때
        if c[i] >=3 : #숫자 i의 개수가 3이상이면
                    # c리스트에는 인덱스의 번호의 수가 저장되어있기 때문에
            c[i] -= 3 # c에서 3을 뺀다 (재 등장을 막기 위해)
            tri += 1 #triplet에 1 추가
            continue #continue/ i는 그대로 3을빼도 아래 경우에 해당할 수 있어서
        if c[i] >= 1 and c[i+1] >=1 and c[i+2]>=1: #i,i+1,i+2가 1 이상이면
            c[i]-=1 #각 값에서 1씩 빼줌
            c[i+1] -= 1
            c[i+2] -= 1
            run += 1 #run에 1 추가
            continue #continue i는 그대로 숫자가 aabbcc같은 형태일수도 있어서
        i+=1
    if run+tri == 2 : print("Baby Gin")
    else : print("Lose")