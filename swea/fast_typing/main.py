T = int(input())
for t in range(1,T+1) :
    a,b = input().split()
    typing = a.split(b)
    typing = 'x'.join(typing)
    print(f'#{t} {len(typing)}')