data = int(input())
cnt = 0
for i in range(data,0,-1) :
    first = data
    lst = [data,i]
    second = i
    etc = first - second
    while etc >= 0 : 
        lst.append(etc)
        first = second
        second = etc
        etc = first - second
        
    cnt_n = len(lst)
    if cnt_n > cnt :
        cnt = cnt_n
        result = lst

final = ' '.join(str(s) for s in result)
print(cnt)
print(final)