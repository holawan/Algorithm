num , res = map(int,input().split())

cnt = 0
while res > num :
    if int(res)%2 :
        if str(res)[-1] == '1' :
            res = str(res)[:-1]
            res = int(res)
        else :
            break
    else :
        res = res//2
    cnt +=1
    if res == num :
        break

if res==num :
    print(cnt+1)
else :
    print(-1)
