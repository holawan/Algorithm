import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lst = [int(input()) for _ in range(n)]

l, r = min(lst), sum(lst)

ans = 10e9

while l <= r:
    k = (l+r)//2

    tmp_k = k
    minus = 1
    idx = 1

    for i in range(n):
        if tmp_k < lst[i]:
            tmp_k = k
            idx += 1
        tmp_k -= lst[i]

    if idx > m or k < max(lst):
        l = k + 1
    else:
        r = k - 1
        ans = k
print(ans)
