x = bin(0x1DB176C588D26EC).replace('0b','0')
print(x)
print(len(x))
x = '1DB176C588D26EC'
# 01110110110001011101101100010110001000110100100110111011
# 01110110110001011101101100010110001000110100100110111011
# b1110110110001011101101100010110001000110100100110
# 011101101100010111011011000101100010001101001001101110
# 0111011
# 0110001
# 0111011
# 0110001
# 0110001
# 0001101
# 0010011
# 0111011
alter_num = {
    'A' : 10, 'B' : 11, 'C' : 12,
    'D' : 13, 'E' : 14, 'F' : 15
}




import sys 
sys.stdin = open('input2.txt','r')


n = int(input())
R,C = map(int,input().split())

grid = [list(input()) for _ in range(R)]

r = 0
c = C-1 
lst = []
codes = [[0,0,0,1,1,0,1],[0,0,1,1,0,0,1],[0,0,1,0,0,1,1],[0,1,1,1,1,0,1],[0,1,0,0,0,1,1],[0,1,1,0,0,0,1],[0,1,0,1,1,1,1],[0,1,1,1,0,1,1],[0,1,1,0,1,1,1],[0,0,0,1,0,1,1]]
while r<R :
    if grid[r][c] != '0' :
        ec = c
        while grid[r][c] != '0' :
            c -= 1
        sc = c+1 
        lst.append(grid[r][sc:ec+1])
    else :
        c-=1 
    if c<0 :
        c = C-1
        r += 1 
binary_num = ''.join(lst[0])
box = [0]*7 



