import sys 

sys.stdin = open('input.txt','r')

for i in range(10) : 
    t = int(input())
    lst = list(map(int,input().split()))
    # lst = [10,6,12,8,9,4,1,3]
    cnt = 0
    while True :
        x= 0 
        if lst[0]-(cnt%5)-1 <0 :
            lst = lst[1:]+[0]
        else :
            lst = lst[1:] + [lst[0]-(cnt%5)-1]
        cnt += 1 

        if lst[-1] == 0 :
            for i in lst :
                if i>=10 :
                    x = 1
                    break 
            else :
                break
        

    print(f'#{t} ',end='')
    for i in lst :
        print(i,end=' ')
    print()

