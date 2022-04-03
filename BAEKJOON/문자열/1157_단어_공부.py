word = input()
#출력 형식에 맞게 단어를 받고 대문자로 변경 
word = word.upper()

#딕셔너리에 넣어서 카운트를 셈 
dic = {}
for w in word :
    if w in dic:
        dic[w] += 1
    else : 
        dic[w] = 1
#문자 담을 리스트
lst = []
lst2 = []
#가장 많이 등장한 단어를 고르기 
M = max(list(dic.values()))

#단어가 두번 등장하면 ?를 출력해야하므로 x를 초기값 0으로 둠  
x = 0

#딕셔너리 키 밸류를 돌면서 
for a,k in dic.items() :
    #키를 리스트에 추가 
    lst.append(a)
    #벨류가 맥스값이면 x+=1 
    if k==M :
        x+=1
    #x가 1보다 크면 맥스값이 2개 이상이므로 ?를 반환하고 리턴 
    if x >1:
        print('?')
        exit()
    #아니면 그냥 lst2에 넣어줌 
    else :
        lst2.append(k)
print(lst[lst2.index(max(lst2))])

