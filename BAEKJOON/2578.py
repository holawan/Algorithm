from pprint import pprint
bingo1 = [list(map(int,input().split()))for i in range(5)]
bingo2 = list(map(list,zip(*bingo1)))

bingo3 = [];bingo4 = []
for i in range(len(bingo1)) :
    bingo3.append(bingo1[i][i])
    bingo4.append(bingo2[i][4-i])
bingo = bingo1+bingo2
bingo.append(bingo3)
bingo.append(bingo4)
lst = []
for i in range(5) :
    lst += list(map(int,input().split()))
j = 0
while n !=3 :
    for b in bingo :
        if bingo in lst[0:j] :
            pass
