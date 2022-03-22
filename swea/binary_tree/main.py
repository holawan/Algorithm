n = int(input())

root = n//2 + 1 


dic = {}
for i in range(1,n+1) :
    dic[i] = i

def heap(x) :
    if x == 1 :
        return
    lst = [dic[x],dic[x//2],dic[x-1]]
    lst.sort()
    dic[x-1],dic[x//2],dic[x] = lst[0],lst[1],lst[2]
    print(dic)
    heap(x//2)
if n%2==0 :
    
    if dic[n]>dic[n//2] :
        dic[n//2],dic[n] = dic[n],dic[n//2]
    print(dic)
    heap(n)
    # for i in range(n-1,1,-2) :
    #     print(dic)
    #     heap(i)
    
else :
    for i in range(n,1,-2):
        heap(i)
print(dic)
print(dic[root],dic[n//2])