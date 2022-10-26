import sys 
import heapq
input = sys.stdin.readline


def union(a,b) :
    a = find(a)
    b = find(b)

    if b< a :
        parent[a] = b 
    else :
        parent[b] = a

def find(x) :
    if x == parent[x] :
        return x 
    parent[x] = find(parent[x])
    return parent[x]

#정점의 수, 간선의 수 
V,E = map(int,input().split())

edge = []

for _ in range(E) :
    a,b,w = map(int,input().split())

    edge.append((w, a, b))

edge.sort(key=lambda x : x[0])

parent = list(range(V+1))
res = 0
for w,s,e in edge :
    # print(w,s,e)
    if find(s) != find(e) :
        union(s,e)
        res += w 
print(res)