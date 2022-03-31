T = int(input())


def quicksort(lst,l,r) :
    if l< r:
        s = partition(lst,l,r)
        quicksort(lst,l,s-1)
        quicksort(lst,s+1,r)

def partition(lst,l,r) :
    p = lst[l]
    i,j = l,r 

    while i<=j :
        while i<=j and lst[i] <=p :
            i+= 1 
        while i<=j and lst[j] >p :
            j -= 1 
        if i<j :
            lst[i],lst[j] = lst[j],lst[i]
    lst[l],lst[j] = lst[j],lst[l]
    return j
for t in range(1,T+1) : 
    n = int(input())

    lst = list(map(int,input().split()))
    quicksort(lst,0,n-1)
    print(f'#{t} {lst[n//2]}')