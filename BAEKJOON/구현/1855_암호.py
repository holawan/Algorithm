n = int(input())
s = input()
l = len(s)
#예제와 같은 행렬을 만든다. 
lst = [[0]*(n) for _ in range(l//n)]

x = -1
#행의 길이만큼 돌면서 
for i in range(l//n) :
    #짝수이면 그대로 넣고 
    if i %2 ==0 :
        for j in range(n) :
            x+=1 
            lst[i][j] = s[x]
    #홀수이면 반대로 넣는다. 
    else :
        for j in range(n-1,-1,-1) :
            x += 1
            lst[i][j] = s[x]
result = []
#열 우선으로 출력한다. 
for j in range(n) :
    for i in range(l//n) :
        result.append(lst[i][j])

print(''.join(map(str,result)))