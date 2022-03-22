import sys
sys.stdin = open('input.txt','r')


def cal(a,b,operator): #연산자에 따라 연산 결과 리턴 
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b
    else:
        return a/b
 
def func(x):
    if tree[x]: #자식이 있으면 
        a = func(tree[x][0]) #해당 자식으로 들어가서 리턴값을 얻음
        b = func(tree[x][1]) #위와 동일 
        return cal(a,b,node[x]) #재귀과정을 거쳐 연산이 되었으면 연산 결과를 맽음
    return int(node[x]) #자식이 없다면 해당 숫자를 리턴 
 
for t in range(1,3):
    n = int(input())
    tree = [[] for _ in range(n+1)] #자식을 담을 트리 리스트 만들기
    node = [0 for _ in range(n+1)] #빈 노드 만들기
    for _ in range(n): #input의 수 만큼 돌면서
        tmp = list(input().split()) # input을 받고
        node[int(tmp[0])] = tmp[1]  #임의의 정점의 연산자 혹은 값을 노드에 번호로 자리에 추가 
        for i in map(int,tmp[2:]):
            tree[int(tmp[0])].append(i)#트리 리스트에는 노드 번호로 자식들을 추가
    print(f'node:{node}')
    print(f'tree:{tree}')
    ans = func(1)
    print(f'#{t} {int(ans)}')