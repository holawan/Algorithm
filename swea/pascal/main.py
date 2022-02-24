

def pascal(n):
    if n <= 0:
        raise IndexError('잘못된 값 입력 양수를 입력하세요')

    elif n == 1:  #첫번째 숫자는 1
        return [1]

    elif n == 2:
        print(*pascal(n-1))
        return [1, 1]

    else:
        lst = pascal(n-1)
        print(*lst)
        result = [1]
        for i in range(1, n - 1):
            result.append(lst[i - 1] + lst[i])
        result.append(1)
        return result


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    print(f'#{t}')
    print(*pascal(n))
