from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    A,B = map(int,input().split())
    q = deque()
    q.append((A,""))
    visit = [0] * 10000
    
    while q:
        num, path = q.popleft()
        visit[num] = True
        if num == B:
            print(path)
            break
        x = (2*num)%10000
        if not visit[x]:
            q.append((x,path+'D'))
            visit[x] = 1

        x = (num-1)%10000
        if not visit[x]:
            q.append((x,path+'S'))
            visit[x] = 1

        x = (10*num+(num//1000))%10000
        if not visit[x]:
            q.append((x,path+'L'))
            visit[x] = 1

        x = (num//10+(num%10)*1000)%10000
        if not visit[x]:
            q.append((x,path+'R'))
            visit[x] = 1