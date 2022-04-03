n = int(input())
for i in range(n) :
    a = int(input())
    b= int(input())


    lst = [[0]*b for i in range(a+1)]
    for i in range(b) :
        lst[-1][i] = i+1

    for i in range(len(lst)-2,-1,-1) :
        for j in range(b) :
            lst[i][j] = sum(lst[i+1][0:j+1])

    print(lst[-a-1][b-1])