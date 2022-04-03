#10보다 작을경우를 대비해서 문자로 받는다.
N = input()

#길이가 1이면 0을 붙이고 각자리를 더한다. 
if len(N) < 2 :
    N = '0' + N
a = int(N[0]) + int(N[1])

#주어진 수의 가장 오른쪽과 앞에서 구한 합의 오른쪽을 붙인다.
if len(str(a)) <2 :
    x = N[1] + str(a)
else :
    x = N[1] + str(a)[-1]

#숫자가 돌아올때까지 연산을 반복한다. 

#한번했으므로 카운트는 1부터 시작 
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