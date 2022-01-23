a = int(input())
arr = []
for _ in range(a): 
	arr.append(list(map(int, input().split())))


def facto(x) :
    result = 1 
    for i in range(1,x+1) :
        result *=i 
    return result
    

for coc in arr :
    if coc[0] == coc[1] :
        print(1)
    else :
        result = facto(coc[1]) / (facto(coc[0]) * facto(coc[1]-coc[0]))
        print(int(result))


