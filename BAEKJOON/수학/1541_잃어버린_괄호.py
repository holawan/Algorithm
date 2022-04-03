#- 로 분리 
data = input().split('-')

s1 = []

#가장 작은값을 하려면 뒤에가 커져야하기 때문에 +형태를 다 더해줌 
for i in data :
    data2 = i.split('+')
    s = 0
    for j in data2 :
        s += int(j)
    s1.append(s)
#앞에서부터 빼줌 
result = s1[0]
for i in s1[1:] :
    result -= i
print(result)