import sys 
sys.stdin = open('input.txt','r')

T = int(input())

#회전 수 
K = int(input())

m1 = list(map(int,input().split()))
m2 = list(map(int,input().split()))
m3 = list(map(int,input().split()))
m4 = list(map(int,input().split()))
m_lst = [m1,m2,m3,m4]
#회전 시키려는 자석, 자석 번호 
score = 0 
direction = [-1,1]


def dfs(i) :
    
    for k in range(2) :
        global score,m_lst
        new_i = i+direction[k] 
        if 0<=new_i<4 and not visited[new_i] :
            visited[new_i] = 1
            if i<new_i :
                if m_lst[i][2] != m_lst[new_i][-2] :
                    m_lst[new_i] = m_lst[new_i][1:] + [m_lst[new_i][0]]
                    dfs(new_i)
                else :
                    return
            else :
                if m_lst[i][-2] != m_lst[new_i][2] :
                    m_lst[new_i] = m_lst[new_i][1:] + [m_lst[new_i][0]]
                    dfs(new_i)
                else :
                    return

for k in range(K) :
    rotation_num , dir = map(int,input().split())
    rotation_num -= 1 
    visited  =[0]*4
    visited[rotation_num] = 1
    dfs(rotation_num) 
    if dir == 1 :
        m_lst[rotation_num] = [m_lst[rotation_num][-1]] + m_lst[rotation_num][:7]
        print(f'k:{m_lst}')
    else :
        m_lst[rotation_num] = m_lst[rotation_num][1:] + [m_lst[rotation_num][0]]
        print(f'k:{m_lst}')
        print(1)

for i in range(4) :
    if m_lst[i][0] == 1 :
        score += 2**i
print(score)