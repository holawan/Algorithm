import sys
n = int(sys.stdin.readline())
N_lst = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
M_lst = list(map(int,sys.stdin.readline().split()))

N_lst.sort()

def binary_search(x) :
    start = 0
    end = n-1 

    while start <= end :
        mid = (start+end)//2
        
        if N_lst[mid] == x :
            return True
        
        elif x <N_lst[mid] :
            end = mid -1

        else :
            start = mid +1
    return False 

for x in M_lst :
    print(int(binary_search(x)))
