a,b = map(str,input().split())
lst1 = [a]
lst2 = [b]

if  '5' in a:
    lst1.append(a.replace('5','6'))
if '6' in a :
    lst1.append(a.replace('6','5'))

if '5' in b :
    lst2.append(b.replace('5','6'))
if '6' in b :
    lst2.append(b.replace('6','5'))

lst1.sort();lst2.sort()

print(int(lst1[0])+int(lst2[0]),int(lst1[-1])+int(lst2[-1]))