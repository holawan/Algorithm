arr = []
for i in range(2) :
    arr.append(int(input()))

x = str(arr[1])

print(arr[0] * int(x[2]))
print(arr[0] * int(x[1]))
print(arr[0] * int(x[0]))
print(arr[0]*arr[1])