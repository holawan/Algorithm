duck = input()
lst=  [] 
for i in duck :
    lst.append(i)

ori = 'quack' 

j = 0
result = []
while True :
    if lst[0] == ori[j] :
        result.append(lst.pop(0))
        if j <len(ori)-1 :
            j+=1 
        else :
            j-=4
    else :
        lst.pop(0)
    if lst == [] :
        break

print(len(result)//len(ori))