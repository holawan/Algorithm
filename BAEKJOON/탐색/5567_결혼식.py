import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

members = [[0]*(n+1) for _ in range(n+1)]
visited = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    members[a][b] = 1
    members[b][a] = 1
fof = []
fof2 = []
cnt = 0
for i in range(2, n+1):
    if members[1][i]:
        cnt += 1
        visited[1][i] = 1
        visited[i][1] = 1
        fof.append(i)

for friend in fof:
    for i in range(2, n+1):
        if members[friend][i] and not visited[friend][i] and not (i in fof or i in fof2):
            cnt += 1
            visited[friend][i] = 1
            visited[i][friend] = 1
            fof2.append(i)

print(cnt)
