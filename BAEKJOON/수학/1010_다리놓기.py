a = int(input())
arr = []
#데이터입력
for _ in range(a): 
	arr.append(list(map(int, input().split())))


def func(x) :
    result = 1 
    for i in range(1,x+1) :
        result = result * i 
    return result
    
#nCr 조합 형태로 해결 
#1이면 1 리턴 
#1이 아니면 n!/(n-r)! * r!
for coc in arr :
    if coc[0] == coc[1] :
        print(1)
    else :
        result = func(coc[1]) / (func(coc[0]) * func(coc[1]-coc[0]))
        print(int(result))

