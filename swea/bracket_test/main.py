T = int(input())

for t in range(1,T+1) : 
    case = list(input())
    #스택 만들기 인덱스 에러 방지용 x넣음
    stack = ['x']
    #top은 0 
    top = 0
    #여는 괄호 
    test = ['(','{']
    y = 1 
    #텍스트를 돌면서 
    for s in case : 
        #문자가 여는 괄호이면 
        if s in test :
            #스택에 추가 
            stack.append(s)
            top += 1  
        else :
            #스택이 비어있는데 닫는 괄호가 들어오면 y에 0을 리턴하고 종료 
            if stack[top] == 'x' and s in [')','}'] :
                y = 0 
                break
            #닫는 괄호이면서 스택의 맨 위가 여는 괄호이면 
            elif s == ')'  :
                if stack[top] == '(' : 
                    stack.pop()
                    top-=1 
                else :
                    y = 0 
                    break 

            #닫는괄호이면서 스택의 맨 위가 여는 괄호이면 case 2 
            elif s == '}'  :
                if  stack[top] == '{' :
                    stack.pop()
                    top -= 1
                else :
                    y = 0 
                    break  

    if stack[top] == 'x' and y == 1   :
        print(f'#{t} 1')
    else :
        print(f'#{t} 0')