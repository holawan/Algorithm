

n = int(input())
hash = input()
result = 0
for i in range(n) :
    result+= (ord(hash[i])-96)*31**i
print(result%1234567891)