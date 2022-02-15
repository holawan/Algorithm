want = int(input())

x = 64
lst = [x]
cnt = 0
while sum(lst)!= want:
    lst.append(lst.pop(-1)/2)
    if sum(lst) >= want :
        continue
    else : 
        lst.append(lst[-1])

print(len(lst))
    