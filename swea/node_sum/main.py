import sys

sys.stdin = open('input.txt','r')


T = int(input())

for t in range(1,T+1) : 
    #노드 수와 주어진 잎의 수, 찾을 값 받기
    node, leaf, L = map(int,input().split())

    #딕셔너리 만들기
    dic = {}
    #잎을 돌면서 노드 번호를 key로 값을 value로 받음
    for _ in range(leaf) :
        key,value = map(int,input().split())
        dic[key] = value

    #역순으로 돌면서 
    for i in range(node,0,-1):

        #i가 key안에 있으면 멈추기 
        if i in dic.keys():
            continue
        #dictionary에 i가 없으면 
        else :
            #노드 길이가 key*2+1한 값보다 작거나 같으면 
            #해당 노드의 값은 자식 두개를 합한 것 
            if i*2+1 <= node :
                dic[i] = dic[i*2]+dic[i*2+1]
            #노드 길이가 i*2+1보다 작을 때는 
            # 자식이 하나밖에 없기 때문에 그 값을 저장  
            else :
                dic[i] = dic[i*2]

    print(f'#{t} {dic[L]}')
