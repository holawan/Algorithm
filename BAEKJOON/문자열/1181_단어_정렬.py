#문자의 수 받는다. 
n = int(input())
#문자들을 다 리스트에 넣는다. 
lst = [input() for i in range(n)]
#중복제거를 위해 set을 사용하고 다시 리스트로 바꾼다. 
lst = list(set(lst))
#리스트를 사전순으로 정렬한다. 
lst.sort()
#리스트를 길이 순으로 정렬한다.(사전순으로 후에)
lst2 = sorted(lst,key=len)
for word in lst2:
    print(word)