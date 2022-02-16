n = int(input())
s = input()
l = len(s)
lst = [[0]*(n) for _ in range(l//n)]

x = -1
for i in range(l//n) :
    if i %2 ==0 :

        for j in range(n) :
            x+=1 
            lst[i][j] = s[x]
    else :
        for j in range(n-1,-1,-1) :
            x += 1
            lst[i][j] = s[x]
result = []
for j in range(n) :
    for i in range(l//n) :
        result.append(lst[i][j])

print(''.join(map(str,result)))