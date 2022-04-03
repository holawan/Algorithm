#현재x,현재y,꼭지점x,꼭지점y
x,y,x2,y2 = map(int,input().split())


#아래위 꼭지점 
lst = [0,x2,0,y2]

#현위치에서 거리를 계산할 lst
lst2 = []

#x축 차를 계산 
for l in lst[:2] :
    lst2.append(abs(x-l))
#y축 차를 계산 
for l in lst[2:] :
    lst2.append(abs(y-l))

#최소값 리턴 
print(min(lst2))
