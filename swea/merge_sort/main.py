from collections import deque

def merge_sort(lst):
    if len(lst) == 1:
        return lst

    middle = len(lst)//2

    return merge(deque(merge_sort(lst[:middle])), deque(merge_sort(lst[middle:])))


def merge(left, right):
    global cnt 
    result = []
    if left[-1]>right[-1] :
        cnt += 1 
    while left or right:

        if left and right:
            if left[0] <= right[0]:
                result.append(left.popleft())
            else:
                result.append(right.popleft())
        elif left:
            result.extend(left)
            break
        elif right:
            result.extend(right)
            break

    return result

T = int(input())

for t in range(1,T+1) : 
    n = int(input())
    lst = list(map(int,input().split()))
    cnt = 0 
    res = merge_sort(lst)
    print(f'#{t} {res[n//2]} {cnt}')
