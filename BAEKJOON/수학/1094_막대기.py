#원하는 길이 
want = int(input())

#막대기의 길이 
x = 64
#막대기를 리스트에 넣는다. 
lst = [x]

#내가 자른게 원하는 값이 아니면 
while sum(lst)!= want:
    #반절로 자른 막대를 리스트에 담는다.(하나는 임시로 버린다고 가정)
    lst.append(lst.pop()/2)
    #자른 막대중에 하나를 버리고 남은 막대의 길이 합이 원하는 값보다 크거나 같으면 다음으로
    if sum(lst) >= want :
        continue
    #아니라면 리스트에 막대 추가 
    else : 
        lst.append(lst[-1])

#막대기들의 길이를 구함
print(len(lst))
    