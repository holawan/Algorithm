n,k = map(int,input().split())
lst = [i+1 for i in range(n)]
result = []

#리스트 생성
idx = 0
#마지막 숫자가 남을때까지
for i in range(n-1) :
	#0베이스 고려 idx에 k-1을 추가한다.
	idx += k-1
	#리스트의 길이보다 idx가 크면 idx를 lst로 나눈 나머지를 idx로 사용한다. 
	if idx >=len(lst) :
		idx %= len(lst)
	#결과 리스트에 해당 index의 값을 넣고 제거한다.
	result.append(lst.pop(idx))

result += lst


result = f'<{result}>'
result = result.replace('[','')
print(result.replace(']',''))