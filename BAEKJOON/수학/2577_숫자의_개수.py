#숫자를 받아온 후 곱하고 문자로 변환한다.
lst = [] 
for i in range(3) :
    lst.append(int(input()))
x = str(lst[0]*lst[1]*lst[2])

#자리수를  돌면서 개수를 출력한다.
for i in range(10) :
    print(x.count(str(i)))