import sys
#sys.stdin = open("input.txt","r")
board = [list(map(int, input().split())) for _ in range(7)]
count = 0
for i in range(3):
    for j in range(7):
        temp = board[j][i:i+5]
        if temp == temp[::-1]:
            count += 1
        for k in range(2):
            if board[i+k][j] != board[4+i-k][j]:
                break
        else:
            count+=1
print(count)
#!!!!!!!!!!!!!!!!!!!!!!다시 풀어보기!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!