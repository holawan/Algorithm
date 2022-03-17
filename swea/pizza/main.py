import sys 
sys.stdin = open('input.txt','r')

from collections import deque

T = int(input())
for t in range(1,T+1) : 
    #화덕 크기와 피자의 수
    size,num = map(int,input().split())

    #치즈 받아오기 
    cheese = list(map(int,input().split())) 
    pizza = []
    #피자 번호와 치즈수를 넣은 피자리스트 만들기
    for i in range(num) :
        pizza.append([i+1,cheese[i]])
    print(pizza)
    #화덕의 크기만큼 큐에 넣기
    que = deque(pizza[:size])

    last = size
    #큐가 빌때까지 
    while que :
        #큐에서 가장 앞의 피자를 빼서
        x = que.popleft()
        #치즈를 2로 나눈 몫으로 바꿈
        x[1] //= 2 
        #치즈가 남았다면 
        if x[1]>0 :
            #큐에 다시 넣기
            que.append(x)
        #치즈가 다 녹았을 때 마지막 피자가 아니면 
        #큐에 남아았는 피자를 추가 
        elif last <num :
            last += 1 
            que.append(pizza[last-1])
        
    print(f'#{t} {x[0]}')
