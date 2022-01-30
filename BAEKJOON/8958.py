N =  int(input())
for n in range(N) :
    score = input()
    i = 0
    x = 0
    result= []
    while i <len(score) : 
        if score[i] == 'X' :
            x = 0
        else : 
            x += 1
        result.append(x)
        i +=1

    print(sum(result))