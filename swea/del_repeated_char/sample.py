tcs = int(input())
#test case 숫자 받기
for tc in range(1, tcs+1):
    s = input()
    # string 받기
    stack = []
    # stack으로 삼을 리스트 생성
    top = -1
    # 빈 stack의 top의 값 -1
    stack.append('dummy')
    top += 1
    stack.append(s[0])
    top += 1
    #반복문을 돌리면서 string들의 각 character를 stack의 인덱스를 통해 비교를 하려면
    #stack을 채우고 인덱스가 적어도 0이 되게 해야합니다
    #하지만 top = 0에서 멈출경우 range Error가 떠서 dummy를 넣어서 top = 1상태로 for문을 시작할 수 있게 했습니다
 
 
    for c in s[1::]:
        # 반복문을 돌리기전에 string의 첫자리를 이미 stack에 넣었으므로, 둘쨋 자리부터 반복문을 돌리는데
        if c == stack[top]:
            stack.pop()
            top -= 1
            #stack에 가장 최근 push한 character와 string의 해당 순서의 character가 같다면
            # stack의 가장 최근 charactor를 pop해주고 top도 1 감소시킨다
        else:
            stack.extend(c)
            top += 1
            #if문에 해당하지 않을경우 stack에 string의 해당 순서의 character를 push 해준다
 
 
    print(f'#{tc} {top+1-1}')
    #top의 값은 stack의 원소가 0 개일때 -1이므로, stack 원소의 갯수는 top+1이 된다.
    #그리고 제일 처음에 dummy data로 인해 실제 top의 값에 +1이 되어 있으므로 -1을 해준다
