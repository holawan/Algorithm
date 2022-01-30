N = input()

if len(N) < 2 :
    N = '0' + N
a = int(N[0]) + int(N[1])

if len(str(a)) <2 :
    x = N[1] + str(a)
else :
    x = N[1] + str(a)[-1]
cnt = 1 
while x != N :
    if len(x) <2 :
        x = '0' + x
    a = int(x[0]) + int(x[1])
    if len(str(a)) <2 :
        x = x[1] + str(a)
    else :
        x = x[1] + str(a)[-1]
    cnt += 1
print(cnt)