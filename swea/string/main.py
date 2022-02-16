import sys

sys.stdin = open('input.txt','r')

def BruteForce2(p,t) :
    i = 0
    j = 0
    cnt = 0
    for i in range(n-m + 1) :
        match = 0
        for j in range(m) :
            if t[i+j] != p[j]:
                break
            else :
                match +=1
        if match == m :
            cnt += 1

    return cnt
for _ in range(1,11) :
    T = int(input())
    p = input()
    t = input()
    n = len(t)
    m = len(p)
    print(f'{T} {BruteForce2(p,t)}')