from pickle import NONE
import sys 

sys.stdin = open('input.txt','r')

for t in range(1,11) :

    n = int(input())

    tree = [[0,0] for _ in range(n+1)]

    lst = [list(input().split()) for _ in range(n)]
    tree[0] = None


    for x in lst :
        parents = int(x[0])
        if len(x) == 2 :
            continue
        elif len(x) == 3 :
            tree[parents][0] = int(x[2])
        elif len(x) == 4 :
            tree[parents][0] = int(x[2])
            tree[parents][1] = int(x[3])

    start = 1
    visited = [0]*(n+1)
    def search(tree,start) :

        if tree[start][0] :
            search(tree,tree[start][0])
        visited[start]
        print(lst[start-1][1],end='')
        if tree[start][1] :
            search(tree,tree[start][1])

    print(f'#{t} ',end='')
    search(tree,start)
    print()