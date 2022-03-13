
T = int(input())
for t in range(T) :
    n = int(input())
    lst = []
    for i in range(n) :
        x = input()
        lst.append(x)
    lst.sort()
    res = 'YES'
    for i in range(n-1) :
        if lst[i] == lst[i+1][:len(lst[i])] :
            res = 'NO'
            print(res)
            break
    else :
        print(res)