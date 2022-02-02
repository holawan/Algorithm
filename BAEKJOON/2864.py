a,b = map(str,input().split())
lst1 = [a]
lst2 = [b]
for num in a :
    if num == '5':
        lst1.append(a.replace('5','6'))
    elif num == '6':
        lst1.append(a.replace('6','5'))
for num in b :
    if num == '5':
        lst2.append(b.replace('5','6'))
    elif num == '6':
        lst2.append(b.replace('6','5'))

lst1.sort();lst2.sort()

print(int(lst1[0])+int(lst2[0]),int(lst1[-1])+int(lst2[-1]))