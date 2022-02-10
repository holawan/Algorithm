n = int(input())
num_lst = []
for i in range(1,n+1) :
    num = i
    SUM = sum(map(int,str(i)))
    if SUM+i == n :
        print(i)
        break
    if i == n :
        print(0)
