lst = [] 
for  i in range(9) :
    lst.append(int(input()))
#숫자의 최대값을 구하고 
print(max(lst))
#제로베이스 고려 인덱스에 1을 더한 값을 출력한다. 
print(lst.index(max(lst))+1)