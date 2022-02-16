import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T) :
    ts, num = input().split()
    lst = input().split()
    #각 숫자의 수를 담을 딕셔너리를 만듭니다.
    box = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR':0, 'FOR':0, 'FIV':0, 'SIX':0, 'SVN':0, 'EGT':0, 'NIN':0}
    #섞여있는 수자 리스트를 돌며, 해당 숫자가 키인 사전 요소에 value를 1씩 추가합니다.
    for i in lst :
        box[i] += 1

    # key와 value를 돌며 key를 value개 만큼 인쇄합니다.

    for key,value in box.items() :
        print(f'{key} '* value)