import sys 

sys.stdin = open('input.txt','r')


T = int(input())

for t in range(1,T+1) : 
    n,m = map(int,input().split())

    #배열 만들기 
    grid = [list(map(int,input())) for _ in range(n)]
    #변환해줄 코드 리스트 
    codes = [[0,0,0,1,1,0,1],[0,0,1,1,0,0,1],[0,0,1,0,0,1,1],[0,1,1,1,1,0,1],[0,1,0,0,0,1,1],[0,1,1,0,0,0,1],[0,1,0,1,1,1,1],[0,1,1,1,0,1,1],[0,1,1,0,1,1,1],[0,0,0,1,0,1,1]]
    #행순환 
    for i in range(n) :
        #모든 코드가 뒤가 1이라서 열을 역으로 순환하면서 1인 값을 찾고 해당 j 값에서 55를 뺀 값이 시작 지점 
        for j in range(m-1,-1,-1) :
            if grid[i][j] == 1 :
                s_i,s_j = i,j-55
                break

    #암호 목록 
    password = grid[s_i][s_j:s_j+56]
    #암호를 분리해줄 리스트
    lst = []
    #숫자로 변환해서 넣어줄 리스트
    code = 0 

    #7칸씩 뛰면서 암호 분리 
    for i in range(0,56,7) :
        lst.append(password[i:i+7])
    #암호가 코드의 인덱스와 일치하면 해당 인덱스로 정답 부여 
    for i in range(8) :
        for j in range(10) :
            if lst[i] == codes[j] :
                if i %2 :
                    code += j
                break
    
    #홀수는 *3 짝수는 그대로인데 제로베이스니까 여기서는 짝수일때 *3 
    code = 0
    for i in range(len(ans)) :
        if i%2 :
            code += ans[i]
        else :
            code += 3 * ans[i]

    #10으로 나눌 때 나머지가 있으면 0 
    if code%10 :
        print(f'#{t} 0')
    else :
        print(f'#{t} {sum(ans)}')