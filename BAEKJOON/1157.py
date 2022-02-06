word = input()

word = word.upper()

dic = {}
for w in word :
    if w in dic:
        dic[w] += 1
    else : 
        dic[w] = 1
lst = []
lst2 = []
M = max(list(dic.values()))

x = 0
for a,k in dic.items() :
    lst.append(a)
    if k==M :
        x+=1
    if x >1:
        print('?')
        exit()
    else :
        lst2.append(k)
print(lst[lst2.index(max(lst2))])

