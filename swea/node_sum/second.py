import sys 
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1) : 
    #노드의 개수 N, 리프노드 수 M, 값을 출력할 노드 L
    N,M,L = map(int,input().split())

    #리프노드들로 딕셔너리 만들기 
    node_dic = {}
    for i in range(M) :
        a,b = map(int,input().split())
        node_dic[a] = b
    print(f'leaf_node: {node_dic}')
    #홀수일때는 
    if N%2 : 
        #루트에 갈때까지 
        while N>1 :
            #부모노드는 자식노드들의 합 
            node_dic[N//2] = node_dic[N] +node_dic[N-1]
            N -=2
            print(f'node: {node_dic}') 
    #짝수일 때는 
    else :
        #자식노드 한개는 홀수이므로 처리 해주고 
        node_dic[N//2] = node_dic[N]
        N -= 1 
        print(f'node: {node_dic}') 
        #루트에 갈 때까지 
        while N>1 :
            #부모노드는 자식노드들의 합 
            node_dic[N//2] = node_dic[N] + node_dic[N-1]
            N -=2 
            print(f'node: {node_dic}') 
    print(f'#{t} {node_dic[L]}')