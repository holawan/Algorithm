def solution(s):
    answer = 0
    lst = ['zero','one','two','three','four','five','six','seven','eight','nine']
    lst2 = ['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(lst)) :
        s = s.replace(lst[i],lst2[i])
    answer = int(s)
    return answer

