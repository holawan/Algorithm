n = int(input())

root = n//2 + 1 


tree = [0]*(n+1)
ch1 = [0]*(n+1)
ch2 = [0]*(n+1)

for i in range(1,n+1) :
    tree[i] = i
    child = i 
    parents = i//2

    while parents>=1 and tree[child]>tree[parents] :
        tree[child],tree[parents] = tree[parents],tree[child]
        child = parents
        parents = child//2

print(tree)


