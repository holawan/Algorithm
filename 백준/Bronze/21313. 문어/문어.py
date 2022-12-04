n = int(input())
lst = []

if n % 2:
    for i in range(n-1):
        if i % 2:
            lst.append(2)
        else:
            lst.append(1)
    lst.append(3)
else:
    for i in range(n):
        if i % 2:
            lst.append(2)
        else:
            lst.append(1)

print(*lst)
