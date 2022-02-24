import sys 
sys.stdin = open('input.txt','r')
T = int(input())
for t in range(1,T+1) :
    n,m = map(int,input().split())

    n_lst = list(map(int,input().split()))
    m_lst = list(map(int,input().split()))

    #n리스트보다 m리스트가 길다는 가정을 만들기 위한 조건문
    if len(n_lst)>len(m_lst) :
        n_lst,m_lst = m_lst,n_lst
        n,m = m,n 

    my_max = 0
    j = 0
    while j+n <= m :
        my_sum = 0
        for i in range(n) :
            my_sum += n_lst[i]*m_lst[j+i]
        if my_sum >my_max :
            my_max = my_sum 
        j += 1 
    print(f'#{t} {my_max}')