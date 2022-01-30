N = int(input())
n = N
for i in range(N) : 
    word = input()
    lst = []
    j = 0
    while word != '' :
        if word[j] in lst :
            n -= 1 
            break
        else :
            lst.append(word[j])
            word = word.lstrip(word[j])
print(n)