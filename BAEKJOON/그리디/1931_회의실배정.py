import sys
n = int(sys.stdin.readline())
lst = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]


#시작시간을 기준으로 선정렬 
lst.sort(key=lambda x:x[0])

#종료시간 기준으로 정렬 
lst.sort(key = lambda x:x[1])

#이렇게 정렬했을 때 종료시간이 같을 때 시작시간 오름차순으로 정렬된다. 

cnt = 1
#첫회의의 시작점이 기준 
conference = lst[0][1] 
#두번째 회의부터 돌면서 
for i in range(1,n) :
    #다음회의 시간의 시작이 현재 종료보다 크거나 같으면 cnt += 1 
    if lst[i][0] >= conference:
        cnt +=1
        #그 회의의 종료시간을 기준으로 갱신 
        conference = lst[i][1]
print(cnt)