initial = int(input())
swi = list(map(int,input().split(' ')))
num = int(input())
arr = []
for _ in range(num): 
	arr.append(list(map(int, input().split(' '))))

for a in arr :
    if a[0] == 1 :  #남자일 때
        for i in range(a[1]-1,len(swi),a[1]) : #a[1]-1 인덱스부터 끝까지 a[1]배만큼 순회하며 스위치를 변경
            if swi[i] == 1 :
                swi[i] = 0
            else :
                swi[i] = 1 
    else : #여자이면 
        j = 0  
        if swi[a[1]-1] == 1 : #해당 스위치를 변경
            swi[a[1]-1] = 0
        else : 
            swi[a[1]-1] = 1
        while  ((a[1]-j-2) >= 0) and ((a[1]+j) < (len(swi))):  #여자가 받은 숫자의 좌우 인덱스가 0보다 크거나 같으면서 스위치의 총 길이보다 작으면
            if swi[(a[1]-j-2)] == swi[(a[1]+j)] : #좌우가 같을 때
                if swi[(a[1]-j-2)] == 1 : #값 반대로 입력
                    swi[(a[1]-j-2)] = 0 
                    swi[a[1]+j] = 0
                else :
                    swi[(a[1]-j-2)] = 1
                    swi[a[1]+j] = 1
                j += 1
            else : #좌우가 다르면 멈추기 
                break

result = ' '.join(str(s) for s in swi)
for i in range(0,len(result),40) :
    print(result[i:i+40])