import sys

sys.stdin = open('input.txt','r')

for t in range(1,11) :                  #테스트 케이스만큼
    dump = int(input())                 #dump 횟수
    box = list(map(int,input().split())) #박스 리스트

    #Buble sort
    for i in range(len(box)-1,0,-1) : #박스를 뒤에서부터 순회하며
        for j in range(i) :            #0부터 i까지
            if box[j] > box[j+1] : #박스가 그 뒤 박스보다 크면
                box[j],box[j+1] = box[j+1],box[j] #위치 변경
    #덤프 시작

    for flatten in range(dump) :
        #박스의 맨 처음 값에 1 더하고 마지막 값에 1을 뺌
        box[0] += 1 ; box[-1] -=1
        if box[0] > box[1] :
            box[0],box[1] = box[1],box[0]
        if box[-2] > box[-1] :
            box[-2],box[-1] = box[-1],box[-2]
    print(box)
    print(f'#{t} {box[-1]-box[0]}')