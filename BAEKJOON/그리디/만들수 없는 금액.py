n =5 

lst = [3,1,1]

lst.sort()

target = 1 

for i in lst :
    if target < i :
        break 
    target += i

print(target)