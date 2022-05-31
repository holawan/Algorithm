a,b,n=map(int, input().split())
a%=b
# print(a,b)
for i in range(n-1):
    a=(a*10) % b
    # print(a)
print((a*10) // b)