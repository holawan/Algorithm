x = 0 
while True : 
    a,b = map(int,input().split())
    if a == 0 & b== 0 :
        x = 1
        break
    else :
        print(a+b)