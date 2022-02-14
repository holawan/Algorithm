t = int(input())

for i in range(t) :
    R, B, M = map(float,input().split())
    n = 0
    R =  0.01*R

    while B > 0 :
        print(B,M,R)
        n+=1
        new_R = round(B*R,2)
        B += new_R
        print(B)
        B -= M
        print(B)
        if n>1200 :
            n = 'impossible'
            break
        print(B,M,R)
    print(n)
