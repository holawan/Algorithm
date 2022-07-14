
def solve(n) :
    if n ==0 :
        return [1,0] 
    elif n==1 :
        return [0,1] 
    else :
        before = [1,0]
        after = [0,1]

        for _ in range(1,n) :
            answer = [before[0]+after[0],before[1]+after[1]]
            before = after
            after = answer 
        return answer  

T = int(input())



for t in range(T) :
    n = int(input())
    print(solve(n)[0],solve(n)[1])

    
'''
0 = 1,0
1 = 0,1 
2 = 1,1
3 = 1,2
4 = 2,3
5 = 3,5
6 = 5,8
7 = 8,13
'''