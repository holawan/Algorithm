a,b = map(int,input().split()) 
num = int(input())
lst = [list(map(int, input().split())) for _ in range(num)] 

rec_list = [0 for i in range(2*num)]
print(rec_list)
for i in lst :
    if lst[0] == 0 :
        pass