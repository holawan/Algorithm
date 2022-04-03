import sys
from collections import Counter

n = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(n)]
lst.sort()


mean = round(sum(lst)/n)

median = lst[n//2]

cnt_lst = Counter(lst).most_common()

range_ = lst[-1]-lst[0]


print(mean)
print(median)
if len(cnt_lst)>1 and cnt_lst[0][1] == cnt_lst[1][1] :
    print(cnt_lst[1][0])
else : 
    print(cnt_lst[0][0])
print(range_)
        

