T = int(input())

for tc in range(1,T+1) :
    s = list(input())
    t = list(input())
    

    lst = []
    for i in range(2) :
        for j in range(len(s)) :
            tmp = s[j]
            s[j] = str(i)
            x = ''.join(s)
            lst.append(int(x,2))
            s[j] = tmp
    for i in range(3) :
        for j in range(len(t)) :
            tmp = t[j]
            t[j] = str(i)
            x = ''.join(t)
            if int(x,3) in lst :
                break 
            t[j] = tmp 
    print(f'#{tc} {int(x,3)}')
