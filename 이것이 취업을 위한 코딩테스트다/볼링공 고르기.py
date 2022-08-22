N,M = map(int,input().split())

ball = list(map(int,input().split()))

lst = []


cnt = 0 
for i in range(len(ball)) :
    for j in range(i+1,len(ball)) :
        if i!=j and ball[i] != ball[j] :
            cnt += 1


print(cnt)