N = int(input())

count = 0
while True :
    #5로 나눠지면 cnt에 5로 나눈 몫을 더하고 멈춤 
    if N%5 ==0 :
        count += N//5
        break
    #아니면 3빼는데 정확히 못맞추면 -1리턴 
    else :
        if N-3 >=0 :
            N-=3 
            count +=1
        else :
            count = -1
            break
print(count)