import sys
sys.stdin = open('input.txt','r')

def dfs(city) : #도시 방문 재귀함수
    visited[city] = 1 #도시에 도착했으면 도착 표시 1
    if city == 99 :
        return
    for next_city in range(100) :  #도시들을 순회하며
        if grid[city][next_city] == 1 and not(visited[next_city]) : #이동가능하며, 아직 방문하지 않았다면
            dfs(next_city) #해당 도시로 이동

for _ in range(1,11) :
    t,node = map(int,input().split()) #테스트 케이스 번호와, 노드의 수
    grid = [[0]*100 for _ in range(100)] #이동가능 경우를 나타낼 배열
    visited = [0]*100 #방문 확인

    lst = list(map(int,input().split())) #노드 리스트 받기
    for i in range(0,node*2,2) : #한칸씩 띄워가며 경로 받기
        grid[lst[i]][lst[i+1]] = 1 #이동 가능하면 1로 표시
    dfs(0)  #0번 도시에서 출발

    if visited[99] == 1 : #도착지인 99번 도시에 방문했다면
        print(f'#{_} 1')
    else :
        print(f'#{_} 0')
# for g in grid :
#     print(g)
