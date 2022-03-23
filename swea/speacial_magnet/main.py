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
                else :
                    return
            else :
                if m_lst[i][-2] != m_lst[new_i][2] :
                    m_lst[new_i] = m_lst[new_i][1:] + [m_lst[new_i][0]]
                else :
                    return
print(m_lst)
for k in range(K) :
    rotation_num , dir = map(int,input().split())
    rotation_num -= 1 
    lst = []
    for i in range(3) :
        if m_lst[i][2] != m_lst[i+1][-2] :
            lst.append(i)
        else :
            break
    for i in lst :
        m_lst[i+1] = m_lst[i+1][1:] + [m_lst[i+1][0]]
    if dir == 1 :
        m_lst[rotation_num] = [m_lst[rotation_num][-1]] + m_lst[rotation_num][:7]
    else :
        m_lst[rotation_num] = m_lst[rotation_num][1:] + [m_lst[rotation_num][0]]

for i in range(4) :
    if m_lst[i][0] == 1 :
        score += 2**i
print(score)