import pprint 
arr = []
for _ in range(4): 
	arr.append(list(map(int, input().split())))
print(arr)

square_list = [] 
for a in arr :
    area = 0 
    square_list.append(abs((a[2]-a[0])*(a[3]-a[1])))
print(square_list)


grid = [[0]*10 for _ in range(10)]
pprint.pprint(grid)
for i in range(len(arr)) :
      for j in range(arr[i][1],arr[i][3]+1) :
          grid[i][arr[i][j]] = 1 
      for k in range(arr[i][0],arr[i][2]+1) :    
          grid[i][arr[i][j]] = 1 

pprint.pprint(grid)
