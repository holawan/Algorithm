from itertools import combinations

L, C = map(int,input().split())

alpha = list(input().split())

alpha.sort()
m = ['a','e','i','o','u']

comb = combinations(alpha,L)

for c in comb :
    cntm = 0 
    for i in c :
        if i in m :
            cntm += 1 
    if 0< cntm <= L-2 :
        print(''.join(c)) 