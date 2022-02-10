M, win = map(int,input().split())
number = list(map(int,input().split()))
lst = []
for i in range(len(number)-2): 
    for j in range(i+1,len(number)-1) :
        for k in range(j+1,len(number)) :
            lst.append(number[i]+number[j]+number[k])

#number리스트를 순회하며, 가능한 세 수의 합의 모든 경우의 수를 더해 리스트에 담음 

lst.append(win) #딜러가 선언한 숫자를 더함 
lst.sort() #리스트를 정렬 
if lst[lst.index(win)] == lst[-1]: #만약 딜러가 선언한 수가 리스트의 마지막 값이면
    print(lst[-2]) #리스트의 -2번째 원소를 출력 
elif lst[lst.index(win)+1] == win : #리스트 내부 딜러가 선언한 수 다음 값이 딜러가 선언한 값과 같으면
    print(win) #딜러가 선언한 값 출력
else :
    print(lst[lst.index(win)-1]) #둘다 아니면 딜러가 선언한 값의 전 수를 출력 

