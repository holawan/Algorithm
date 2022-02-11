n = int(input())
lst = [input() for i in range(n)]
lst = list(set(lst))
lst.sort()
lst2 = sorted(lst,key=len)
for word in lst2:
    print(word)