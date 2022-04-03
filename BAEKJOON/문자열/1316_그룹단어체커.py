N = int(input())
#단어의 수를 받아온다. 
n = N

#단어의 길이만큼 반복하며 단어를 받고 
for i in range(N) : 
    word = input()
    lst = []
    j = 0
    #단어가 빌때까지 while을 도는데 
    while word != '' :
        #이미 리스트에 단어가 있으면 멈춘다. 
        if word[j] in lst :
            n -= 1
            break
        #아니면 단어를 리스트에 넣어주고 해당 단어를 제거한다.
        else :
            lst.append(word[j])
            word = word.lstrip(word[j])
print(n)