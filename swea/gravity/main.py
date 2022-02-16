import sys

sys.stdin = open('input.txt','r')

n = int(input())
for i in range(n) :
    N = int(input())
    lst = list(map(int,input().split()))
    for j in range(len(lst),-1,-1) :
        if lst[j] == 0 :
            continue
        lst[j] > lst[j-1]
