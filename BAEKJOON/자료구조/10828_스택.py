a = int(input())
arr = []
for _ in range(a): 
	arr.append(input().split())

stack = []
for i in arr :
	if i[0] == 'push' :
		stack.append(int(i[1]))
	elif i[0] == 'top' :
		if len(stack) >0 :
			print(stack[-1]) 
		else : 
			print(-1)
	elif i[0] == 'size' :
		print(len(stack))
	elif i[0] == 'empty' :
		if len(stack) > 0 :
			print(0)
		else :
			print(1)
	else : 
		if len(stack) == 0:
			print(-1)
		else :
			print(stack[-1]) 
			del stack[-1]