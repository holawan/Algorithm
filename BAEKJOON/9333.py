t = int(input())
import math

for i in range(t) :
    R, B, M = map(float,input().split())
    n = 0
    R =  0.01*R
    while B > 0 :
        n+=1
        new_R = str(round(B*R,4))
        new_R = round(float(new_R),2)
        B += new_R
        B -= M
        if n>1200 :
            n = 'impossible'
            break
    print(n)
