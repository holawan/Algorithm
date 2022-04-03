n = int(input())

for i in range(1,n+1) :
    num = i
    #숫자를 문자로 바꾼 후 sum을 해서 자리수별합을 구한다. 
    s = sum(map(int,str(i)))
    if s+i == n :
        print(i)
        break
    if i == n :
        print(0)
    print(i)
