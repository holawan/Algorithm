s = list(input())
bomb = list(input())
#스택 만들기 
stack = []
#문자를 돌면서 
for i in range(len(s)) :
    #스택에 넣기 
    stack.append(s[i])
    #stack의 뒤에서 폭발문자의 길이만큼 인덱싱해서 폭발문자와 같다면 
    if stack[-(len(bomb)):] == bomb :
        #폭발문자의 길이만큼 pop 
        for _ in range(len(bomb)) :
            stack.pop()
if stack :
    print(''.join(stack))
else :
    print('FRULA')