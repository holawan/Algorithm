from tkinter import N


n = int(input())
lst = []
for i in range(n):
	a,b = input().split()
	lst.append([int(a),b])

lst.sort(key=lambda x:x[0])
for l in lst :
	print(*l)