# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.8.10
    A.sort()
    start = A[0] 
    print(A)
    if A[0] != 1 :
        return 1 
    A = list(set(A))
    print(A)

    for x in A[1:] :
        print(x)
        if x - start == 1 :
            start = x 
        else :
            return x-1
    return A[-1]+1



print(solution([1, 3, 6, 4, 1, 2]),
solution([1,2,3]),
solution([-1,-3]))