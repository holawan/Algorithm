T = int(input())

for t in range(1,T+1) :
    #문자열 받기 
    char = input()
    #stack 생성
    stack = []
    #빈 stack의 top 값은 -1 
    top = -1 
    stack.append('dummy')
    top += 1 
    stack.append(char[0])
    top += 1 

    #만약 문자열의 0번째와 1번째 index가 같으면 
    #스택에 남은 요소가 없어져 비교가 불가능하기 때문에 더미를 하나 넣어줌 

    for s in char[1:] :
        #스택에 0번째 요소가 들어가 있으니까 두번째 요소부터 돌림 
        #현재 문자와 스택의 마지막요소가 같으면
        if s == stack[top] :
            #중복이므로 stack.pop 
            stack.pop()
            top -=1 
        else :
            stack.append(s) 
            top += 1 
            #아니면 스택에 추가 

    #top의 초기값이 -1이므로 길이를 계산하려면 top에 +=1 
    #초기에 추가해준 dummy 빼기 
    print(f'#{t} {top +1 -1}')