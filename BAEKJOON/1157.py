word = input()

word = word.upper()
print(word)

dic = {}
for w in word :
    if w in dic:
        dic[w] += 1
    else : 
        dic[w] = 1
lst = []
for a,k in dic.items() :
    lst.append[[a,k]]

