alpha = 'abcdefghijklmnopqrstuvwxyz'
dic = {}
for i in range(len(alpha)) :
    dic[alpha[i]] = i+1

n = int(input())
x = input()
result = 0
for i in range(n) :
    result += dic[x[i]] *31 **i
print(result%1234567891)


