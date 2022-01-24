length = int(input())
a = list(input() for _ in range(length))
for i in a :
    if i[0] == ')' or i[-1] =='(' :
        print('NO')
    elif i.count('(') == i.count(')') :
        if i[0:int(len(i)/2)].count(')') >= (len(i)/4) :
            print('NO')
        else :
            print('YES')
    else :
        print('NO')
