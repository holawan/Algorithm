n ,room = map(int,input().split())

lst = list([] for _ in range(12))
print(lst)
print([]*12)
exit()

for i in range(n) :
    sex,grade = map(int,input().split())
    if sex==1 :
        lst[grade-1].append(1)
    else :
        lst[grade+5].append(1)

lst3=[]
for search in lst :
    search.remove(0)
    if search==[] :
        continue
    lst3.append(search)

for search in lst3 :
    if len(search)>room :
        lst2 = []
        while len(search)>room :
            search.remove(1)
            lst2.append(1)
        lst3.append(lst2)

print(len(lst3))