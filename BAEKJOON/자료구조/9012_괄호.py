length = int(input())
a = list(input() for _ in range(length))
for i in a  :
    while i.find('()') != -1 :
        i = i.replace('()','')
    if len(i) >0 :
        print('NO')
    else :
        print('YES')