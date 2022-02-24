T = int(input())
for t in range(1, T + 1):

    node, line = map(int, input().split())
    graph = [[0]*(node + 1) for _ in range(node + 1)]

    for i in range(line):
        a, b = map(int, input().split())
        graph[a][b] = 1
    s,g= map(int, input().split())
    stack = [s]
    visited = [s]

    while stack:
        tmp = stack[-1]

        for n in range(1, node+ 1):
            if graph[tmp][n] == 1 and n not in visited :
                visited.append(n)
                stack.append(n)
                break
        else:
            stack.pop()
    # print(visited)
    if g in visited:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')